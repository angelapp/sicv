from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import datetime

from mailjet_rest import Client


from sicv.settings import *

from .models import *


# Create your views here.

class cerrar_sesion(View):
    
    def get(self, request):
        auth_logout(request)
        return  redirect('programas')
    


class iniciar_sesion(View):
    
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if request.user.groups.filter(name='Estudiantes').exists():
                return redirect('/')
            else:
                return redirect('/admin')
        else:
            return render(request, 'iniciar-sesion.html', {'credentialError':True})


    def get(self, request):
        return render(request, 'iniciar-sesion.html', {})


class programas(View):
    
    def get(self, request):
        programas = Programa.objects.filter(activo = True)
        return render(request, 'programas.html', {'programas':programas})
        
        
class contactenos(View):
    
    def post(self, request):
        nombre = request.POST.get('name', '')
        email = request.POST.get('email', '')
        telefono = request.POST.get('phone', '')
        comentarios = request.POST.get('comments', '')
        programa = request.POST.get('programm', '')
        programa = get_object_or_404(Programa, pk=programa)
        contacto = Contacto(nombre=nombre, email=email, telefono=telefono, comentarios=comentarios, programa=programa)
        contacto.save()
        programas = Programa.objects.filter(activo = True)
        return render(request, 'contactenos.html', {'programas':programas, 'guardado':True})

    def get(self, request):
        programas = Programa.objects.filter(activo = True)
        return render(request, 'contactenos.html', {'programas':programas})



class detalle_programa(View):

    def get(self, request, id):
        programa = Programa.objects.filter(id = id)
        nop = False
        noc = False
        insc = False
        fin = False
        maxc = False
        
        if 'nop' in request.session:
            nop = request.session['nop']
            request.session['nop'] = False

        if 'noc' in request.session:
            noc = request.session['noc']
            request.session['noc'] = False

        if 'insc' in request.session:
            insc = request.session['insc']
            request.session['insc'] = False

        if 'fin' in request.session:
            fin = request.session['fin']
            request.session['fin'] = False

        if 'maxc' in request.session:
            maxc = request.session['maxc']
            request.session['maxc'] = False


        if len(programa) > 0:
            context = {'cursos':programa[0].cursos.all(), 'programa':programa[0], 'nop': nop, 'noc':noc, 'fin':fin,'insc':insc, 'maxc':maxc}
        else:
            context = ""
        return render(request, 'detalle-programa.html', context)



class inscribir(View):
    
    def get(self, request, id_programa, id_curso):
        nop = validate_programa(request.user,id_programa)
        noc = validate_curso(request.user,id_programa, id_curso)
        fin = validate_finalizado(request.user,id_programa, id_curso)
        maxc = validate_maxcurso(request.user,id_programa)
        request.session['nop'] = nop
        request.session['noc'] = noc
        request.session['fin'] = fin
        request.session['maxc'] = maxc
        if not nop and not noc and not fin and not maxc:
            programa = Programa.objects.filter(id = id_programa)
            curso = Curso.objects.filter(id = id_curso)
            curso_usuario = CursoUsuario(fecha_inscripcion = datetime.datetime.now(), 
            usuario = request.user, curso = curso[0], programa = programa[0], status = 'cursando')
            curso_usuario.save()
            request.session['insc'] = True
            ##Enviar Email al coordinador
            mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_SECRET_KEY), version='v3.1')
            data = {
            'Messages': [
                {
                "From": {
                    "Email": "m_a15@hotmail.es",
                    "Name": "Mario"
                },
                "To": [
                    {
                    "Email": programa[0].cordinador.email,
                    "Name": programa[0].cordinador.first_name
                    }
                ],
                "Subject": "Hola " + programa[0].cordinador.first_name + ", el estudiante con código " + request.user.codigo + " ha inscrito un curso",
                "TextPart": "",
                "HTMLPart": "<h1>Hola " + programa[0].cordinador.first_name + "</h1> <p>Es estudiante con código " + request.user.codigo + " ha inscrito el curso "+ curso[0].nombre +" para el programa " + programa[0].nombre + "</p>"
                }
            ]
            }
            result = mailjet.send.create(data=data)
            print (result.status_code)
            print (result.json())
           
        return redirect('detalle_programa', id=id_programa)
            

def validate_finalizado(usuario, id_programa, id_curso):
    programa = Programa.objects.filter(id = id_programa)
    curso = Curso.objects.filter(id = id_curso)
    
    if len(curso) > 0 and len(programa) > 0:
        cursos_usuarios = CursoUsuario.objects.filter(usuario = usuario, curso = curso[0], programa = programa[0])
        return len(cursos_usuarios) > 0
    else:
        return True


def validate_curso(usuario, id_programa, id_curso):
    programa = Programa.objects.filter(id = id_programa)
    curso = Curso.objects.filter(id = id_curso)
    
    if len(curso) > 0 and len(programa) > 0:
        if curso[0].curso_pre:
            cursos_usuarios = CursoUsuario.objects.filter(status = 'finalizado', usuario = usuario, curso = curso[0].curso_pre, programa = programa[0])
            return len(cursos_usuarios) == 0
        else:
            False
    else:
        return True

def validate_programa(usuario, id_programa):
    programa = Programa.objects.filter(id = id_programa)
    if len(programa) > 0 :
        progama_usuario = ProgramaUsuario.objects.filter(status = 'cursando', usuario__id = usuario.id, programa=programa[0])
        return len(progama_usuario) == 0
    else:
        return True

def validate_maxcurso(usuario, id_programa):
    programa = Programa.objects.filter(id = id_programa)
    if len(programa) > 0 :
        progama_usuario = ProgramaUsuario.objects.filter(status = 'cursando', usuario__id = usuario.id, programa=programa[0])
        
        if len(progama_usuario) > 0:
            cursos_usuario = CursoUsuario.objects.filter(status = 'cursando', usuario = usuario, semestre = progama_usuario[0].semestre, programa = programa[0])
            curso_semestre = CursoSemestre.objects.filter(programa = programa[0], semestre = progama_usuario[0].semestre)
            if len(curso_semestre) > 0:
                print(curso_semestre[0].max_curso)
                print(len(cursos_usuario))
                return len(cursos_usuario) >= curso_semestre[0].max_curso
            else:
                return True
        else:
            return True
    else:
        return True
    
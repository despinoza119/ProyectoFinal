from django.shortcuts import render
from django.http import HttpResponse
from .models import Basket,Avatar
from .forms import BasketFormulario,UserRegisterForm,UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def futbol(request):
    return render(request,"AppCoder/futbol.html")

def basket(request):
    return render(request,"AppCoder/basket.html")

def tenis(request):
    return render(request, "AppCoder/tenis.html")

def post1(request):
    return render(request, "AppCoder/post1.html")

def post2(request):
    return render(request, "AppCoder/post2.html")

def acerca(request):
    return render(request, "AppCoder/acerca.html")

def inicioBasket(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppCoder/inicioBasket.html", {"url": avatares[0].imagen.url})

def construccion(request):
    return render(request, "AppCoder/construccion.html")

##############CRUD READ###########

def leerBasket(request):
    basket = Basket.objects.all()

    contexto = {"basket":basket}

    return render(request,"AppCoder/leerBasket.html",contexto)



def basketFormulario(request):
    if request.method=='POST':
        miFormulario = BasketFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            basket=Basket(nombre_equipo=informacion['nombre_equipo'],entrenador=informacion['entrenador'],fundacion=informacion['fundacion'],apodo=informacion['apodo'],ubicacion=informacion['ubicacion'],)
            basket.save()

            return render(request,"AppCoder/regresar.html")

    else:
        miFormulario=BasketFormulario()

    return render(request,"AppCoder/basketFormulario.html",{"miFormulario":miFormulario})

def eliminarBasket(request,basket_nombre):

    basket = Basket.objects.get(nombre_equipo=basket_nombre)
    basket.delete()

    baskets = Basket.objects.all()

    contexto={"baskets":baskets}

    return render(request,"AppCoder/regresar.html",contexto)

def editarBasket(request,basket_nombre):

    basket=Basket.objects.get(nombre_equipo=basket_nombre)

    if request.method=='POST':
        miFormulario = BasketFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            basket.nombre_equipo=informacion['nombre_equipo']
            basket.entrenador = informacion['entrenador']
            basket.fundacion= informacion['fundacion']
            basket.apodo = informacion['apodo']
            basket.ubicacion = informacion['ubicacion']

            basket.save()

            return render(request,"AppCoder/regresar.html")
    else:
        miFormulario=BasketFormulario(initial={'nombre_equipo':basket.nombre_equipo, 'entrenador':basket.entrenador, 'fundacion':basket.fundacion, 'apodo':basket.apodo, 'ubicacion':basket.ubicacion })

    return render(request,"AppCoder/basketFormulario.html",{"miFormulario":miFormulario,"basket_nombre":basket_nombre})

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')

            user=authenticate(username=usuario,password=contra)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request,"AppCoder/inicioBasket.html", {"url":avatares[0].imagen.url})
            else:
                return render(request,"AppCoder/inicio.html", {"mensaje":"Error,datos incorectos"})
        else:
            return render(request,"AppCoder/inicio.html", {"mensaje":"Error,formulario erroneo"})

    form=AuthenticationForm()

    return render(request,"AppCoder/login.html",{'form':form})

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html",{"mensaje":"Usuario Creado"})
    else:
        form=UserRegisterForm()
    return render(request,"AppCoder/registro.html",{"form":form})


def editarPerfil(request):

    usuario=request.user

    if request.method=='POST':
        miFormulario=UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data

            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password1']
            usuario.save()
            avatares = Avatar.objects.filter(user=request.user.id)
            return render(request,"AppCoder/inicioBasket.html",{"url":avatares[0].imagen.url})
    else:

        miFormulario=UserEditForm(initial={'email':usuario.email})

    return render(request,"AppCoder/editarPerfil.html",{"miFormulario":miFormulario,"usuario":usuario})

#def inicio(request):
    #avatares = Avatar.objects.filter(user=request.user.id)
    #return render(request,"AppCoder/inicioBasket.html", {"url":avatares[0].imagen.url})
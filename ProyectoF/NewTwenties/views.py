from django.shortcuts import render
from .models import * 
from django.http import HttpResponse, HttpRequest
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

#Clientes

def cliente (req, nombre, apellido, numero):
    
    cliente = Clientes(nombre=nombre, apellido=apellido, numero=numero)
    cliente.save()
    
    return HttpResponse(f"""
        <p>Cliente: {cliente.nombre} {cliente.apellido} AGREGADO!</p>                 
    """) 

def lista_clientes(req):
    
    lista = Clientes.objects.all()
    
    return render(req, "lista_clientes.html", {"lista_clientes": lista})

#Inicio

def inicio (req):
    
    return render (req, "inicio.html")

#Agregar

def agrega_textil(req, producto, tipo, precio):
    
    textil = Textiles(producto=producto, tipo=tipo, precio=precio)
    textil.save()
    
    return HttpResponse(f"""
        <p> Textil: {textil.producto} - {textil.tipo} - ${textil.precio} AGREGADO</p>        
    """)


def agrega_accesorio (req, producto, tipo, precio):
    
    accesorio = Accesorios(producto=producto, tipo=tipo, precio=precio)
    accesorio.save()
    
    return HttpResponse(f"""
        <p> Accesorio: {accesorio.producto} - {accesorio.tipo} - ${accesorio.precio} AGREGADO</p>        
    """)   
    
    #Administradores
    
def administrador_textiles(req: HttpRequest):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        lista_textil = Textiles.objects.all()
        agregarTextil = AdministradorTextiles(req.POST)
        
        if agregarTextil.is_valid():
            print(agregarTextil.cleaned_data)
            data = agregarTextil.cleaned_data
            
            textil = Textiles(producto=data["producto"], tipo=data["tipo"], precio=data["precio"])
            textil.save()
            return render(req, "lista_textiles.html", {"lista_textiles": lista_textil, "mensaje_textil": "Producto agregado correctamente"})
        else:
            return render(req, "lista_textiles.html", {"lista_textiles": lista_textil, "mensaje_textil": "El producto no pudo ser agregado"})
    else:
        agregarTextil = AdministradorTextiles()
        return render(req, "administrador_textiles.html", {"agregarTextil": agregarTextil}) 

def administrador_accesorios(req: HttpRequest):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        lista_accesorio = Accesorios.objects.all()
        agregarAccesorio = AdministradorAccesorios(req.POST)
        
        if agregarAccesorio.is_valid():
            print(agregarAccesorio.cleaned_data)
            data = agregarAccesorio.cleaned_data
            
            accesorio = Accesorios(producto=data["producto"], tipo=data["tipo"], precio=data["precio"], imagen = data ["imagen"] )
            accesorio.save()
            return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio, "mensaje_accesorio": "Accesorio agregado correctamente"})        
        else:
            return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio, "mensaje_accesorio": "El accesorio no pudo ser agregado"})    
    else:
        agregarAccesorio = AdministradorAccesorios()    
        return render(req, "administrador_accesorios.html", {"agregarAccesorio": agregarAccesorio}) 
    
#Listas

def lista_textiles(req):
    
    lista_textil = Textiles.objects.all()
    
    return render(req, "lista_textiles.html", {"lista_textiles": lista_textil})


def lista_accesorios(req):
    
    lista_accesorio = Accesorios.objects.all()
    
    return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio})

#Eliminar

def eliminarTextil(req, id):
    
    if req.method == 'POST': 
        
        textil = Textiles.objects.get(id=id)
        textil.delete()
       
        lista_textiles = Textiles.objects.all()
        
        return render(req, "lista_textiles.html", {"lista_textiles": lista_textiles})

def eliminarAccesorio(req, id):
    
    if req.method == 'POST': 
        
        accesorio = Accesorios.objects.get(id=id)
        accesorio.delete()
       
        lista_accesorios = Accesorios.objects.all()
        
        return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorios})
    
#Editar
    
def editarTextil(req, id):
    lista_textil = Textiles.objects.all() 
    textil= Textiles.objects.get(id=id)
    
    if req.method == 'POST':
        
        agregarTextil = AdministradorTextiles(req.POST)
        
        if agregarTextil.is_valid():
            
            print(agregarTextil.cleaned_data)
            data = agregarTextil.cleaned_data
        
            textil.producto = data["producto"]
            textil.tipo = data["tipo"]
            textil.precio = data["precio"]
            
            textil.save()
            return render(req, "lista_textiles.html", {"lista_textiles": lista_textil, "mensaje_textil": "Producto actualizado correctamente"})    
        else:
            return render(req, "lista_textiles.html", {"lista_textiles": lista_textil, "mensaje_textil": "El producto no pudo ser actualizado"})    
    else:
        agregarTextil = AdministradorTextiles(initial={
            "producto": textil.producto,
            "tipo": textil.tipo,
            "precio": textil.precio,
                
        })       
        return render(req, "editar_textil.html", {"agregarTextil": agregarTextil, "id": textil.id}) 
    
    
def editarAccesorio(req, id):
    lista_accesorio = Accesorios.objects.all() 
    accesorio = Accesorios.objects.get(id=id)
    
    if req.method == 'POST':
        
        agregarAccesorio = AdministradorAccesorios(req.POST)
        
        if agregarAccesorio.is_valid():
            
            print(agregarAccesorio.cleaned_data)
            data = agregarAccesorio.cleaned_data
        
            accesorio.producto = data["producto"]
            accesorio.tipo = data["tipo"]
            accesorio.precio = data["precio"]
            
            accesorio.save()
            return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio, "mensaje_accesorio": "Accesorio actualizado correctamente"})    
        else:
            return render(req, "lista_accesorios.html", {"lista_accesorios": lista_accesorio, "mensaje_accesorio": "El accesorio no pudo ser actualizado"})    
    else:
        agregarAccesorio = AdministradorAccesorios(initial={
            "producto": accesorio.producto,
            "tipo": accesorio.tipo,
            "precio": accesorio.precio,
                
        })       
        return render(req, "editar_accesorio.html", {"agregarAccesorio": agregarAccesorio, "id": accesorio.id}) 
    

def administrador (req):
  return render (req, "administrador.html")

def textiles (req):
    
    textil = Textiles.objects.all()
    
    return render(req, "textiles.html", {"textiles": textil})

def accesorios(req):
    
    accesorio = Accesorios.objects.all()
    
    return render(req, "accesorios.html", {"accesorios": accesorio})

#Login

def loginUsuario (req): 
    
    if req.method == "POST":
        
        miFormulario = AuthenticationForm(req, data= req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user= authenticate(username=usuario, password=psw)

            if user is not None:
                login(req,user)
                return render(req,"inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render (req, "inicio.html", {"mensaje": "Datos incorrectos"})
        else : 
            return render (req, "inicio.html", {"mensaje": "Formulario inválido"})
        
    else: 
            miFormulario = AuthenticationForm()
            return render (req, "login.html", {"miFormulario" : miFormulario})    
    
def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]

            miFormulario.save()

            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito."})

        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFomulario": miFormulario})

#Busqueda
    
def busquedaTextil(req):
  busqueda= req.GET.get("buscar")  
  
  textiles = Textiles.objects.all()  
  
  
  if busqueda :
    textiles = Textiles.objects.filter(
            Q(tipo__icontains = busqueda)

        )

   
    if textiles:
      return render(req,"resultado_PT.html", { "textiles": textiles})
        
    elif textiles:
            return render (req,"resultado_PT.html",{"textiles": textiles})
        
    else: 
            return render (req,"resultado_PT.html", {"mc": "Producto no encontrado"})
  else:
    return render(req,"buscar_PT.html")


def busquedaAccesorios(req):
  busqueda= req.GET.get("buscar2")
  accesorios=Accesorios.objects.all()
  
  if busqueda:
        accesorios =Accesorios.objects.filter(
        Q(tipo__icontains = busqueda)
       
        )
        
        if accesorios :
            return render(req,"resultado_AC.html", {"accesorios":accesorios})
        
        else: 
            return render (req,"resultado_AC.html", {"mc": "Accesorio no encontrado"})
  else:
      return render(req,"buscar_AC.html")
  
#Resultado

def resultadoAccesorios(req):
    return render (req, "resultado_PT.html")


def  resultadoAC(req):
    return render (req,'resultado_AC.html')

#Carrito

def carrito(req): 
    return render (req,"carrito.html")

#About me

def aboutme (req):
     return render (req, "aboutme.html")

#CRUD

class AccesoriosList(ListView):
    model = Accesorios
    template_name = "accesorios_list.html"
    context_object_name = "accesorioslist"
    

class AccesoriosDetail(DetailView):
    model = Accesorios
    template_name = "accesorios_detail.html"
    context_object_name = "accesoriosdetail"


class AccesoriosCreate(CreateView):
    model = Accesorios
    template_name = "accesorios_create.html"
    fields = ("__all__")
    success_url = "/NewTwenties/accesorios-lista/"
    

class AccesoriosUpdate(UpdateView):
    model = Accesorios
    template_name = "accesorios_update.html"
    fields = ("__all__")
    success_url = "/NewTwenties/accesorios-lista/"


class AccesoriosDelete(DeleteView):
    model = Accesorios
    template_name = "accesorios_delete.html"
    success_url = "/NewTwenties/accesorios-lista"

     
#Contacto

def contacto (req):
    if req.method == "POST":
        form = ConsultaFormulario(req.POST)
        if form.is_valid():
            asunto = "Consulta New Twenties"
            mensaje = form.cleaned_data["mensaje"]
            correo = form.cleaned_data ["correo"]
            html = render_to_string("email.html" ,{"mensaje" : mensaje , "correo" : correo})
            from_email= "correo"
           
            send_mail(asunto, mensaje ,from_email , ["twenties.coderhouse@gmail.com"], html_message=html)
           
            return render ( req, "gracias.html")
    else: 
        form = ConsultaFormulario()

        return render (req,"contacto.html", {"form":form})


def gracias(req):
    return render(req,'gracias.html')
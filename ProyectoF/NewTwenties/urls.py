from django.contrib import admin
from django.urls import path
from NewTwenties.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('agrega-cliente/<nombre>/<apellido>/<numero>', cliente),
    path('lista-clientes', lista_clientes),
    path('', inicio, name = "Inicio"),
    path('agrega-textil/<producto>/<tipo>/<precio>', agrega_textil),
    path('administrador-accesorios', administrador_accesorios, name="AdministradorAccesorios"),
    path('administrador-textiles', administrador_textiles, name="AdministradorTextiles"),  
    path('lista-clientes', lista_clientes, name="ListaClientes"),
    path('lista-accesorios', lista_accesorios, name="ListaAccesorios"),  
    path('lista-textiles', lista_textiles, name="ListaTextiles"),  
    path('eliminar-accesorio/<int:id>', eliminarAccesorio, name="EliminarAccesorio"),  
    path('eliminar-textil/<int:id>', eliminarTextil, name="EliminarTextil"),  
    path('editar-accesorio/<int:id>', editarAccesorio, name="EditarAccesorio"),  
    path('editar-textil/<int:id>', editarTextil, name="EditarTextil"),
    path('administrador', administrador, name="Administrador"),  
    path('Clientes', Clientes, name="Clientes"),  
    path('textiles', Textiles, name="Textiles"),  
    path('accesorios', accesorios, name="Accesorios"),  
    path('login', loginUsuario, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name= "inicio.html"), name="Logout"),
    path('buscarPT/', busquedaTextil , name="buscarPT"),
    path('resultadoPT/', textiles , name="resultado"),
    path('buscarAC/', busquedaAccesorios , name="buscarAC"),
    path('resultadoAC/', resultadoAC , name="resultadoAC"),
   
    # //////formulario contacto/////
    
    path('contacto/', contacto , name="contacto"),
    path('gracias/', gracias , name="gracias"),

   
    path('carrito/', carrito , name="carrito"),
    path('aboutme/', aboutme , name="Aboutme"),

    path('accesorios-lista/', AccesoriosList.as_view(), name="AccesoriosLista"),
    path('accesorios-detalle/<pk>', AccesoriosDetail.as_view(), name="AccesoriosDetalle"),
    path('accesorios-crear/', AccesoriosCreate.as_view(), name="AccesoriosCrear"),
    path('accesorios-actualizar/<pk>', AccesoriosUpdate.as_view(), name="AccesoriosActualizar"),
    path('accesorios-eliminar/<pk>', AccesoriosDelete.as_view(), name="AccesoriosEliminar"),
]
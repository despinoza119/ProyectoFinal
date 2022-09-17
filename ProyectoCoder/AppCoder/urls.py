from django.urls import path
from AppCoder import views
from django.contrib import admin

urlpatterns = [
    path('', views.inicio,name='Inicio'),
    path('futbol/', views.futbol,name='Futbol'),
    path('basket/', views.basket,name='Basket'),
    path('tenis/', views.tenis,name='Tenis'),
    path('post1/', views.post1,name='Post1'),
    path('post2/', views.post2,name='Post2'),
    path('acerca/', views.acerca,name='acerca'),
    path('leerBasket/',views.leerBasket, name="LeerBasket"),
    path('basketFormulario/',views.basketFormulario, name="BasketFormulario"),
    path('eliminarBasket/<basket_nombre>/',views.eliminarBasket,name="EliminarBasket"),
    path('editarBasket/<basket_nombre>/',views.editarBasket,name="EditarBasket"),
    path('login/',views.login_request,name='Login'),
    path('register/',views.register,name='Register'),
    path('editarPerfil/',views.editarPerfil,name="EditarPerfil"),
    path('acerca/', views.acerca,name='acerca'),
    path('inicioBasket/', views.inicioBasket,name='inicioBasket'),
    path('construccion/', views.construccion,name='construccion'),
]


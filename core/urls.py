from django.urls import path
from .views import index, galeria, mision, logoutUser, register, registro_insumos, lista_insumos, lista_insumos2, modificar_insumos, eliminar_insumos, ubicacion, loginPage, mision
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('mision/', mision, name="mision"),
    path('registro_insumos/', registro_insumos, name="registro_insumos"),
    path('lista_insumos/', lista_insumos, name="lista_insumos"),
    path('lista_insumos2/', lista_insumos2, name="lista_insumos2"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('mision/', mision, name="mision"),
    path('register/', register, name="register"),
    path('modificar_insumos/<id>/', modificar_insumos, name="modificar_insumos"), 
    path('eliminar_insumos/<id>/', eliminar_insumos, name="eliminar_insumos"),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

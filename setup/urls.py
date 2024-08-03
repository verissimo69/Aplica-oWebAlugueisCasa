
from django.contrib import admin
from django.urls import path
from base import views
from todos.views import list_location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',list_location.lista_locacao, name='listar_locacao'),
]

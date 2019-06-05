# from django.shortcuts import render, redirect
# from .services import usuario_services
# from .forms import UsuarioForm
# from .models import Usuario
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
# # Create your views here.


class Usuarios(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

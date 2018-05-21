from django.contrib import admin
from .models import Post #importa modello definito in model.py

admin.site.register(Post) #Per far si che il nostro modello sia visibile nella pagina di admin

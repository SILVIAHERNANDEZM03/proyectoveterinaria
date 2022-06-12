from django.contrib import admin
from .models import Persona, ClientesFamilia, RelacionPersonasClientes, PacientesMascotas, Vacunas, Pesos

# Register your models here.
admin.site.register(Persona)
admin.site.register(ClientesFamilia)
admin.site.register(RelacionPersonasClientes)
admin.site.register(PacientesMascotas)
admin.site.register(Vacunas)
admin.site.register(Pesos)

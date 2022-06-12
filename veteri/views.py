from rest_framework import viewsets

from .models import Persona
from .serializers import PersonaSerializers

from .models import ClientesFamilia
from .serializers import ClientesFamiliaSerializers

from .models import RelacionPersonasClientes
from .serializers import RelacionPersonasClientesSerializers

from .models import PacientesMascotas
from .serializers import PacientesMascotasSerializers

from .models import Vacunas
from .serializers import VacunasSerializers

from .models import Pesos
from .serializers import PesosSerializers


# Create your views here.
class PersonaViewSet(viewsets.ModelViewSet):
    serializer_class = PersonaSerializers
    queryset = Persona.objects.all()


class ClientesFamiliaViewSet(viewsets.ModelViewSet):
    serializer_class = ClientesFamiliaSerializers
    queryset = ClientesFamilia.objects.all()


class RelacionPersonasClientesViewSet(viewsets.ModelViewSet):
    serializer_class = RelacionPersonasClientesSerializers
    queryset = RelacionPersonasClientes.objects.all()


class PacientesMascotasViewSet(viewsets.ModelViewSet):
    serializer_class = PacientesMascotasSerializers
    queryset = PacientesMascotas.objects.all()


class VacunasViewSet(viewsets.ModelViewSet):
    serializer_class = VacunasSerializers
    queryset = Vacunas.objects.all()


class PesosViewSet(viewsets.ModelViewSet):
    serializer_class = PesosSerializers
    queryset = Pesos.objects.all()
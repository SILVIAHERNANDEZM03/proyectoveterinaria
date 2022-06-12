from rest_framework import serializers
from veteri.models import Persona, ClientesFamilia, RelacionPersonasClientes, PacientesMascotas, Vacunas, Pesos


class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class ClientesFamiliaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientesFamilia
        fields = '__all__'


class RelacionPersonasClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = RelacionPersonasClientes
        fields = '__all__'


class PacientesMascotasSerializers(serializers.ModelSerializer):
    class Meta:
        model = PacientesMascotas
        fields = '__all__'


class VacunasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacunas
        fields = '__all__'


class PesosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pesos
        fields = '__all__'


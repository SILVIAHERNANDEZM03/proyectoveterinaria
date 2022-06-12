from django.db import models

# Create your models here.


class Persona(models.Model):
    nombrepersona = models.CharField(verbose_name='Nombre Persona', max_length=50)
    apellidopersona = models.CharField(verbose_name='Apellido Persona', max_length=100)
    telefono = models.CharField(verbose_name='Teléfono', max_length=20)
    direccion = models.CharField(verbose_name='Dirección', max_length=150)
    email = models.EmailField(verbose_name='Correo Electrónico', max_length=100)

    def _str_(self):
        return self.nombrepersona


class ClientesFamilia(models.Model):
    PrimerApellido = models.CharField(verbose_name='Primer Apellido', max_length=50)
    CuentaBanco = models.CharField(verbose_name='Cuenta de Banco', max_length=20)
    telefono = models.CharField(verbose_name='Teléfono', max_length=20)

    def _str_(self):
        return self.PrimerApellido


class RelacionPersonasClientes(models.Model):
    IDClientesFamilia = models.ForeignKey(ClientesFamilia, verbose_name='ClientesFamilia', on_delete=models.CASCADE)
    IDPersona = models.ForeignKey(Persona, verbose_name='Persona', on_delete=models.CASCADE)

    def _str_(self):
        return self.IDClientesFamilia


class PacientesMascotas(models.Model):
    IDClientesFamilia = models.ForeignKey(ClientesFamilia, verbose_name='ClientesFamilia', on_delete=models.CASCADE)
    AliasMascota = models.CharField(verbose_name='Alias de la mascota', max_length=50)
    Especie = models.CharField(verbose_name='Especie', max_length=50)
    Raza = models.CharField(verbose_name='Raza', max_length=50)
    ColorPelo = models.CharField(verbose_name='Color de pelo', max_length=20)
    FechaNacimiento = models.DateField('dd,mm,aaaa')
    Vacunaciones = models.CharField(verbose_name='Vacunas', max_length=50)

    def _str_(self):
        return self.IDClientesFamilia


class Vacunas(models.Model):
    IDPacientesMascotas = models.ForeignKey(PacientesMascotas, verbose_name='PacientesMascotas', on_delete=models.CASCADE)
    Fecha = models.DateField('dd,mm,aaaa')
    Enfermedad = models.CharField(verbose_name='Enfermedad que tiene', max_length=150)
    FechaProxima = models.DateField('dd,mm,aaaa')

    def _str_(self):
        return self.IDPacientesMascotas


class Pesos(models.Model):
    IDPacientesMascotas = models.ForeignKey(PacientesMascotas, verbose_name='PacientesMascotas',  on_delete=models.CASCADE)
    FechaConsulta = models.DateField(verbose_name='Fecha de consulta')
    Peso = models.CharField(verbose_name='Peso de tu mascota', max_length=10)

    def _str_(self):
        return self.IDPacientesMascotas

from django.db import models

# Create your models here.
kind_types = (
	("k1", "Perro"), 
	("k2", "Gato"),
	("k3", "Canario"),
	("k4", "Hámster")
)

class Owner(models.Model):
	"""docstring for Owner"""
	id = models.AutoField("Id", primary_key=True)
	first_name = models.CharField(verbose_name="Nombres", max_length=100)
	last_name = models.CharField(verbose_name="Apellidos", max_length=200)
	phone = models.CharField(verbose_name= "Teléfono", max_length=15, unique=True)
	address = models.CharField(verbose_name= "Dirección", max_length=100)

	class Meta:
		ordering = ["first_name"]
		verbose_name_plural = "Propietarios"
		verbose_name = "Propietario"

	def __str__(self):
		return "{}".format(self.first_name)

class Pet(models.Model):
	id = models.AutoField("Id", primary_key=True)
	name = models.CharField(verbose_name="Nombres", max_length=100)
	birth_date = models.DateField(verbose_name="Fecha de Nacimiento", auto_now=False)
	weight = models.FloatField(verbose_name="Peso", default=1)
	kind_type = models.CharField(verbose_name="Especie", choices=kind_types, max_length=2)
	description = models.TextField(verbose_name="Descripción", max_length=200)
	owner_id = models.ForeignKey(Owner, verbose_name="Propietario", on_delete=models.CASCADE)
	
	class Meta:
		ordering = ["name"]
		verbose_name_plural = "Mascotas"
		verbose_name = "Mascota"

	def __str__(self):
		return "{}".format(self.name)
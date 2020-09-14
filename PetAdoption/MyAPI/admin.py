from django.contrib import admin
from MyAPI.models import *

# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
	list_display = ("id", "first_name", "last_name", "phone", "address")
	search_fields = ["first_name", "last_name", "phone", "address"]

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
	list_display = ("name", "birth_date", "weight", "kind_type", "description", "owner_id")
	search_fields = ["name", "birth_date", "weight", "kind_type", "description", "owner_id"]
	raw_id_fields = ("owner_id",)
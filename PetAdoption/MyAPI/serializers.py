from rest_framework import serializers
from MyAPI.models import *

class OwnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Owner
		fields = "__all__"

class PetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pet
		fields = "__all__"
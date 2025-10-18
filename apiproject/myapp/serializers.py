from rest_framework import serializers
from .models import Contact



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact            # specify the model name
        fields = ['name', 'title', 'email']  # specify the fields to be serialized

   
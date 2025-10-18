from rest_framework import serializers
from .models import Contact



class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Contact            # specify the model name
        fields = ['name', 'title', 'email', 'url', 'owner']  # specify the fields to be serialized

   
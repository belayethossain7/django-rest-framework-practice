from rest_framework import status
from django.shortcuts import get_object_or_404
from myapp.serializers import ContactSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from myapp.models import Contact

class ContactViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Contact.objects.all()
        contact = get_object_or_404(queryset, pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def create(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        contact = get_object_or_404(Contact, pk=pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        contact = get_object_or_404(Contact, pk=pk)
        contact.delete()
        return Response(status=204)
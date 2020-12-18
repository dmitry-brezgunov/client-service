from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet

from .filters import ContactsFilter
from .models import Client, Contact, Employee
from .renderers import ContactRenderer
from .serializers import (ClientSerializer, ContactCSVSerializer,
                          ContactSerializer, EmployeeSerializer)


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListCSV(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCSVSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('date', )
    filterset_class = ContactsFilter

    renderer_classes = (ContactRenderer, ) + tuple(
        api_settings.DEFAULT_RENDERER_CLASSES)

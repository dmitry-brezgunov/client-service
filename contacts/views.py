from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet

from .filters import ContactsFilter
from .models import Client, Contact, Employee
from .renderers import ContactRenderer
from .serializers import (ClientSerializer, ContactCSVSerializer,
                          ContactSerializer, EmployeeSerializer)


class EmployeeViewSet(ModelViewSet):
    """CRUD для сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=['post'])
    def add_contact(self, request, pk):
        """Добавление связи между сотрудником и клиентом."""
        employee = self.get_object()
        serializer = ContactSerializer(
            data=request.data, context={'employee': employee})

        if serializer.is_valid():
            serializer.save(employee=employee)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientViewSet(ModelViewSet):
    """CRUD для клиентов."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ContactListCSV(ListAPIView):
    """Выгрузка CSV со списком контактов, с фильтрацией по дате."""
    queryset = Contact.objects.all()
    serializer_class = ContactCSVSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('date', )
    filterset_class = ContactsFilter

    renderer_classes = (ContactRenderer, ) + tuple(
        api_settings.DEFAULT_RENDERER_CLASSES)

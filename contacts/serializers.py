from rest_framework import serializers

from .models import Client, Contact, Employee


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Client


class ContactSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """Проверка, что контакт уникален."""
        date = data['date']
        client = data['client']
        employee = self.context['employee']
        contact = Contact.objects.filter(
            date=date, client=client, employee=employee).exists()

        if contact:
            raise serializers.ValidationError('Такой контакт уже существует')
        return data

    class Meta:
        fields = '__all__'
        read_only_fields = ('employee', )
        model = Contact


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('contacts', )
        model = Employee


class ContactCSVSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        fields = ('id', 'employee', 'date', 'client', )
        model = Contact

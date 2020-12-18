from rest_framework import serializers

from .models import Client, Contact, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Client


class ContactSerializer(serializers.ModelSerializer):
    def validate(self, data):
        date = data['date']
        client = data['client']
        employee = data['employee']
        contact = Contact.objects.filter(
            date=date, client=client, employee=employee).exists()

        if contact:
            raise serializers.ValidationError('Такой контакт уже существует')
        return data

    class Meta:
        fields = '__all__'
        model = Contact


class ContactCSVSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        fields = ('id', 'employee', 'date', 'client', )
        model = Contact

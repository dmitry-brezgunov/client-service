from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    adress = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    date = models.DateField()

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='contacts')

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='contacts')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'client', 'employee'], name='unique_contact'
                )
        ]

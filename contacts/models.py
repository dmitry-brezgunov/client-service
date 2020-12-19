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
    contacts = models.ManyToManyField(
        Client, through='Contact', related_name='employees', blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'client', 'employee'], name='unique_contact'
                )
        ]

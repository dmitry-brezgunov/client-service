from rest_framework_csv.renderers import CSVRenderer


class ContactRenderer(CSVRenderer):
    header = [
        'id', 'employee.id', 'employee.name', 'employee.position', 'date',
        'client.id', 'client.name', 'client.age', 'client.adress'
        ]

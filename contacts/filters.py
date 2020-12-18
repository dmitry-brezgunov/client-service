from django_filters import rest_framework as filters

from .models import Contact


class ContactsFilter(filters.FilterSet):
    date_from = filters.DateFilter(
        field_name='date', lookup_expr='gte', input_formats=['%d.%m.%Y'])

    date_to = filters.DateFilter(
        field_name='date', lookup_expr='lte', input_formats=['%d.%m.%Y'])

    class Meta:
        model = Contact
        fields = ('date_from', 'date_to', )

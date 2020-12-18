from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ClientViewSet, ContactListCSV, ContactViewSet,
                    EmployeeViewSet)

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('employees', EmployeeViewSet)
router.register('contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contacts-csv/', ContactListCSV.as_view(), name='contacts-cvs'),
]

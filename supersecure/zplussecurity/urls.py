from django.urls import path
from .views import request_security_key, approve_key_request

urlpatterns = [
    path('request-key/', request_security_key, name='request_key'),
    path('approve-key/<str:employee_id>/', approve_key_request, name='approve_key'),
]

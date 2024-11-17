from rest_framework import serializers
from .models import KeyRequest

class KeyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyRequest
        fields = [
            'id',
            'employee_id',
            'employee_name',
            'employee_email',
            'employee_phone',
            'description',
            'security_key',
            'is_approved',
            'created_at',
        ]
        read_only_fields = ['security_key', 'is_approved', 'created_at']

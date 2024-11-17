from django.db import models
import uuid

class KeyRequest(models.Model):
    employee_id = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=255)
    employee_email = models.EmailField()
    employee_phone = models.CharField(max_length=15)
    description = models.TextField()
    security_key = models.CharField(max_length=255, blank=True, null=True, unique=True)  # Ensure uniqueness
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_security_key(self):
        """Generate a unique security key."""
        self.security_key = str(uuid.uuid4())  # Create a UUID

    def __str__(self):
        return f"{self.employee_name} ({self.employee_id})"

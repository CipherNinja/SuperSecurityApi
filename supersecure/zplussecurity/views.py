from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import KeyRequest
from .serializers import KeyRequestSerializer
from django.db.utils import IntegrityError


@api_view(['POST'])
@permission_classes([AllowAny])
def request_security_key(request):
    """
    Submit a security key request.

    This view handles creating a new key request for the provided employee details.
    """
    data = request.data

    # Validate request data
    required_fields = ["employee_id", "employee_name", "employee_email", "employee_phone", "description"]
    missing_fields = [field for field in required_fields if not data.get(field)]

    if missing_fields:
        return Response(
            {"error": f"Missing required fields: {', '.join(missing_fields)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        # Create the KeyRequest object
        key_request = KeyRequest.objects.create(
            employee_id=data["employee_id"],
            employee_name=data["employee_name"],
            employee_email=data["employee_email"],
            employee_phone=data["employee_phone"],
            description=data["description"],
        )
        return Response(
            {"message": "Request submitted successfully.", "employee_id": key_request.employee_id},
            status=status.HTTP_201_CREATED,
        )
    except IntegrityError:
        return Response(
            {"error": "A request with this employee ID or email already exists."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as e:
        return Response(
            {"error": f"An unexpected error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  # Adjust permissions for GET access
def approve_key_request(request, employee_id):
    """
    Approve a security key request and generate a unique security key.

    For GET requests:
    - Fetch and return the security key if the request is approved.

    For POST requests (Admin only):
    - Approve the request and generate the security key.
    """
    try:
        # Retrieve the KeyRequest object using the employee_id
        key_request = KeyRequest.objects.get(employee_id=employee_id)

        if request.method == 'GET':
            # Check if the key request is approved
            if key_request.is_approved:
                return Response(
                    {"message": "Request already approved.", "security_key": key_request.security_key},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"message": "Request is not approved yet. Please contact the admin."},
                    status=status.HTTP_403_FORBIDDEN
                )

        if request.method == 'POST':
            # Approve the request and generate a security key (Admin access required)
            if not key_request.is_approved:
                key_request.is_approved = True
                key_request.generate_security_key()
                key_request.save()
                return Response(
                    {"message": "Key approved successfully.", "security_key": key_request.security_key},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "Request already approved.", "security_key": key_request.security_key},
                status=status.HTTP_200_OK,
            )

    except KeyRequest.DoesNotExist:
        return Response(
            {"error": "Request not found for the given employee ID. Please check the ID."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        return Response(
            {"error": f"An unexpected error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

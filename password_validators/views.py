from rest_framework.views import APIView
from rest_framework.response import Response

from password_validators.validate_password import validate_password

class ValidatePassword(APIView):
    def post(self, request, *args, **kwargs):
        password = self.request.data["password"]
        validated_password = validate_password(password)

        if isinstance(validated_password, str):
            return Response({"message":validated_password})
        return Response({"password": validated_password})
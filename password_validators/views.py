from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from password_validators.validate_password import validate_password

@api_view(["POST"])
class ValidatePassword(APIView):
    def put(self, request, *args, **kwargs):
        password = self.request.data["password"]
        validate_password = validate_password(password)

        if isinstance(validate_password, str):
            return Response({"message":validate_password})
        return Response({"password": validate_password})
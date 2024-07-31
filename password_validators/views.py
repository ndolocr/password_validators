from rest_framework.views import APIView


class ValidatePassword(APIView):
    def put(self, request, *args, **kwargs):
        password = self.request.data["password"]
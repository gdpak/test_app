from rest_framework                 import status
from rest_framework.views           import APIView
from rest_framework.response        import Response
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required


class IBANGenerator(APIView):
    @method_decorator(login_required)
    def get(self, request, format=None):
        return Response({})

    @method_decorator(login_required)
    def post(self, request, format=None):
        valid_arguments = True
        if valid_arguments:
            return Response({}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

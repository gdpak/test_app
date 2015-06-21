from rest_framework.views           import APIView
from rest_framework.response        import Response
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required

from user_management.iban_generator import IBANGenerator


class IBANGeneratorView(APIView):
    @method_decorator(login_required)
    def get(self, request, format=None):
        return Response({})

    @method_decorator(login_required)
    def post(self, request, format=None):
        generator = IBANGenerator()

        return Response(generator.generate(
            bank         = request.POST.get('generator_bank'   ),
            account      = request.POST.get('generator_account'),
            country_code = request.POST.get('generator_country')))

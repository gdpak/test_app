from json                           import loads
from rest_framework.views           import APIView
from rest_framework.response        import Response
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required

from user_management.models         import UserInformation
from user_management.iban_generator import IBANGenerator


class IBANGeneratorApiView(APIView):
    @method_decorator(login_required)
    def post(self, request, format=None):
        generator = IBANGenerator()

        return Response(generator.generate(
            bank         = request.POST.get('generator_bank'   ),
            account      = request.POST.get('generator_account'),
            country_code = request.POST.get('generator_country')))


class DeleteAccountsApiView(APIView):
    @method_decorator(login_required)
    def post(self, request, format=None):
        try:
            accounts = loads(request.POST['accounts'])
            UserInformation.objects.filter(id__in=accounts).delete()
            return Response({'status': True, 'message': ''})
        except Exception as e:
            return Response({'status': False, 'message': str(e)})

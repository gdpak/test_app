from six                            import string_types
from six                            import iteritems
from django.conf                    import settings
from django.shortcuts               import resolve_url
from django.shortcuts               import render
from django.shortcuts               import redirect
from django.shortcuts               import get_object_or_404
from django.views.generic           import View
from django.core.paginator          import Paginator
from django.core.paginator          import EmptyPage
from django.core.paginator          import PageNotAnInteger
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required

from user_management.forms              import UserInformationForm
from user_management.models             import UserInformation
from user_management.iban_specification import IBAN_SPCIFICATION_CONFIG


class ListAccounts(View):
    template_name = 'list_accounts.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        accounts_list = UserInformation.objects.filter(account_manager=request.user)
        paginator = Paginator(accounts_list, settings.ACCOUNTS_PER_PAGE)

        page = request.GET.get('page')
        try:
            accounts = paginator.page(page)
        except PageNotAnInteger:
            accounts = paginator.page(1)
        except EmptyPage:
            accounts = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {
            "accounts"  : accounts,
            'pages_list': range(1, paginator.num_pages + 1) or [1]})


class CreateAccount(View):
    form_class       = UserInformationForm
    template_name    = 'create_account.html'
    sorted_countries = sorted(IBAN_SPCIFICATION_CONFIG.items(), key=lambda x: x[1].country_name)

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'form'     : self.form_class(),
            'countries': self.sorted_countries
        })

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        data = {
            key : value.strip() if isinstance(value, string_types) else value
            for key, value in iteritems(request.POST)}
        form = self.form_class(data, request.FILES)

        if form.is_valid():
            new_account = form.save(commit=False)
            new_account.account_manager = request.user
            new_account.save()
            return redirect(resolve_url('list_accounts'))
        return render(request, self.template_name, {
            'form'     : form,
            'countries': self.sorted_countries
        })


class UpdateAccount(View):
    form_class       = UserInformationForm
    template_name    = 'update_account.html'
    sorted_countries = sorted(IBAN_SPCIFICATION_CONFIG.items(), key=lambda x: x[1].country_name)

    @method_decorator(login_required)
    def get(self, request, account_id, *args, **kwargs):
        account = get_object_or_404(UserInformation, id=account_id)
        form    = UserInformationForm(instance=account)
        return render(request, self.template_name, {
            'form'     : form,
            'countries': self.sorted_countries
        })

    @method_decorator(login_required)
    def post(self, request, account_id, *args, **kwargs):
        data = {
            key : value.strip() if isinstance(value, string_types) else value
            for key, value in iteritems(request.POST)}
        account = get_object_or_404(UserInformation, id=account_id)
        form    = self.form_class(data, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('list_accounts'))
        return render(request, self.template_name, {
            'form'     : form,
            'countries': self.sorted_countries
        })


class DeleteAccount(View):
    @method_decorator(login_required)
    def get(self, request, account_id, *args, **kwargs):
        account = get_object_or_404(UserInformation, id=account_id)
        account.delete()
        return redirect(resolve_url('list_accounts'))

    @method_decorator(login_required)
    def post(self, request, account_id, *args, **kwargs):
        account = get_object_or_404(UserInformation, id=account_id)
        account.delete()
        return redirect(resolve_url('list_accounts'))

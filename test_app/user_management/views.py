from django.shortcuts               import render
from django.shortcuts               import redirect
from django.contrib.auth            import authenticate
from django.contrib.auth            import login  as auth_login
from django.contrib.auth            import logout as auth_logout
from django.views.generic           import View
from django.contrib.auth.decorators import login_required

from user_management.forms import UserInformationForm


class Index(View):
    template_name = 'index.html'

    @login_required(login_url='/login')
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class Logout(View):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return render(request, self.template_name)


class Login(View):
    form_class    = UserInformationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])

            if user is not None:
                auth_login(request, user)
                return redirect('/')
            return redirect('/login_failure')

from django.conf                    import settings
from django.shortcuts               import resolve_url
from django.shortcuts               import render
from django.shortcuts               import redirect
from django.utils.http              import is_safe_url
from django.contrib.auth            import login
from django.contrib.auth            import logout
from django.views.generic           import View
from django.utils.decorators        import method_decorator
from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth.decorators import login_required


class Index(View):
    template_name = 'index.html'

    @method_decorator(login_required(login_url='/login'))
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class Logout(View):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)


class Login(View):
    form_class    = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form        = self.form_class(request, data=request.POST)
        redirect_to = '/'

        if form.is_valid():
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
            login(request, form.get_user())
            return redirect('/')
        return render(request, self.template_name, {'form': form})

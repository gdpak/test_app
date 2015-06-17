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
from django.views.decorators.csrf   import csrf_protect
from django.views.decorators.cache  import never_cache
from django.views.decorators.debug  import sensitive_post_parameters


class Logout(View):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)


class Login(View):
    form_class    = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class(request)})

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def post(self, request, *args, **kwargs):
        form        = self.form_class(request, data=request.POST)
        next_hop    = request.POST.get('next')
        redirect_to = next_hop if next_hop else resolve_url('index')

        if form.is_valid():
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
            login(request, form.get_user())
            return redirect(redirect_to)
        return render(request, self.template_name, {'form': form})

from django.shortcuts               import render
from django.shortcuts               import redirect
from django.contrib.auth            import logout as auth_logout
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
        auth_logout(request)
        return render(request, self.template_name)


class Login(View):
    form_class    = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('/')
        return redirect('/login', {'form': form})

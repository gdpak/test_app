from django.shortcuts               import render
from django.shortcuts               import redirect
from django.contrib.auth            import authenticate
from django.contrib.auth            import login  as auth_login
from django.contrib.auth            import logout as auth_logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')


def logout(request):
   auth_logout(request)
   return redirect('/login')


def login(request):
    return render(request, 'login.html')


def account_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return redirect('/')
    return redirect('/login_failure')

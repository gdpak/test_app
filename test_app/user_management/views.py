from django.shortcuts               import render
from django.shortcuts               import redirect
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

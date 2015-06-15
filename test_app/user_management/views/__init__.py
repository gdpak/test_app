from django.shortcuts               import render
from django.views.generic           import View
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required


class Index(View):
    template_name = 'index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

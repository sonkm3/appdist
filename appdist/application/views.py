from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import DistApp


def get_server_name(request):
    return request.META['HTTP_HOST']

def root_view(request):
    return redirect('/list/')

@login_required
def list_view(request):
    app_list = DistApp.objects.filter(display=True).order_by('-created')
    return render(request, 'list.html', {'app_list': app_list, 'server_name': get_server_name(request)})

def plistgen_view(request, app_id, updated):
    app = DistApp.objects.get(pk=app_id)
    return render(request, 'app.plist', {'app': app, 'server_name': get_server_name(request)}, content_type='application/octet-stream')


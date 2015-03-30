from django.shortcuts import render, redirect

from .models import DistApp


def get_server_name(request):
    return request.META['HTTP_HOST']

def root_view(request):
    return redirect('/list/')

def list_view(request):
    app_list = DistApp.objects.filter(display=True)
    return render(request, 'list.html', {'app_list': app_list, 'server_name': get_server_name(request)})

def plistgen_view(request, app_id, updated):
    app = DistApp.objects.get(pk=app_id)
    return render(request, 'app.plist', {'app': app, 'server_name': get_server_name(request)}, content_type='application/octet-stream')


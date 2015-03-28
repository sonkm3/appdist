from django.shortcuts import render, redirect

from .models import DistApp


def root_view(request):
    return redirect('/list/')


def list_view(request):
    app_list = DistApp.objects.all()
    return render(request, 'list.html', {'app_list': app_list, 'server_name': request.META['SERVER_NAME']})

def plistgen_view(request, app_id, updated):
    app = DistApp.objects.get(pk=app_id)
    return render(request, 'app.plist', {'app': app, 'server_name': request.META['SERVER_NAME']}, content_type='application/octet-stream')


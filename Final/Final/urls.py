
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.render_template, {'template_name': 'introduction.html'}, name='introduction'),
    path('about_me/', views.render_template, {'template_name': 'about_me.html'}, name='about_me'),
    path('linkedin/', views.render_template, {'template_name': 'linkedin.html'}, name='linkedin'),
    path('github/', views.render_template, {'template_name': 'github.html'}, name='github'),
]
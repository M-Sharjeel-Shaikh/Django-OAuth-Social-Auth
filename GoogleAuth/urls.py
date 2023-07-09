from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

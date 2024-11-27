from django.urls import path
from . import views
from .views import send_email

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
    path('send-email/', send_email, name='send_email'),  # Rota para enviar email
]

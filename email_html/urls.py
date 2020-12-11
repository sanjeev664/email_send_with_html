from django.urls import path
from email_html import views

urlpatterns = [
    path('',views.mail_send),
]

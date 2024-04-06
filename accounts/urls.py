from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.perform_login, name='login'),

]

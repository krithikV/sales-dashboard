# myapp/urls.py
from django.urls import path
from .views import user_login, user_dashboard, user_logout

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('logout/', user_logout, name='user_logout'),
]

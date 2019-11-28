from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.user_login, name='user_login'),
    path('logout/', authapp.user_logout, name='user_logout'),
]

from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.user_login, name='user_login'),
    path('logout/', authapp.user_logout, name='user_logout'),
    path('register/', authapp.user_register, name='user_register'),
    path('update/', authapp.user_update, name='user_update'),
]

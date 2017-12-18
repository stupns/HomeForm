from django.urls import path

from register.views import signup, log, user_logout, index

app_name = 'register'

urlpatterns = [
    path('register/', signup, name='signup'),
    path('login/', log, name='login'),
    path('logout/', user_logout, name='logout'),
    path('',index),
]
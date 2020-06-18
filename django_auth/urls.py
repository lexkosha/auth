from .views import index, login, logout
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'django_auth'
urlpatterns = [
    path('', index, name='index'),
    # path('login/', login, name='login'),
    # path('logout/', logout, name='logout'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
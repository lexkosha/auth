from .views import index, RegisterView, CreateUserProfile
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import login, logout

from django.urls import reverse_lazy
from django.urls import path

app_name = 'django_auth'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(
        template_name='auth/register.html',
        success_url=reverse_lazy('django_auth:profile-create')
    ), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),

]
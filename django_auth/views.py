from .models import UserProfile
# Create your views here.
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login, authenticate
from .forms import ProfileCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from allauth.socialaccount.models import SocialAccount



def index(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['country'] = UserProfile.objects.get().country
        #context['age'] = UserProfile.objects.get(user=request.user).age
        context['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']

    return render(request, 'auth/index.html', context)


class RegisterView(FormView):

    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(username=username,password=raw_password))
        return super(RegisterView, self).form_valid(form)


class CreateUserProfile(FormView):
    form_class = ProfileCreationForm
    template_name = 'auth/profile-create.html'
    success_url = reverse_lazy('django_auth:index')
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('django_auth:login'))
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CreateUserProfile, self).form_valid(form)


# Авторизация пользователя ручная
"""
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse_lazy('django_auth:index'))
    else:
        context = {'form': AuthenticationForm()}
        return render(request, 'auth/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('django_auth:index'))
"""

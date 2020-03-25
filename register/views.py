from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from shops.models import User
from .forms import RegisterForm


# Create your views here.

class ChooseUserTypeView(TemplateView):
    template_name = 'registration/choose_type.html'


class RegisterAsUser(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = User.SHOP_USER
        kwargs['title'] = 'Register as user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 1
        user.save()
        login(self.request, user)
        return redirect('/')


class RegisterAsShopOwner(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = User.SHOP_OWNER
        kwargs['title'] = 'Register as shop owner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 2
        user.save()
        login(self.request, user)
        return redirect('/')

from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from items.models import Category, Items
from .forms import SignUp
import random



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_items = Items.objects.all()
        item_list = list(all_items)
        random_items = random.sample(item_list, 5)
        context['random_items'] = random_items
        return context

class ShopView(ListView):
    template_name = 'Shop.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        category_name = 'Home_Decor'
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            category = None
        if category:
            return Items.objects.filter(Category=category)
        return []

class SignupView(FormView):
    template_name = 'SignupLogin.html'
    form_class = SignUp
    success_url = '/login/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect('core:index')

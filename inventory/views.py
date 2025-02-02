from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from . forms import UserRegisterForm, MainInventoryForm
from . models import MainInventory, Type
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages

# Create your views here.
class Index(TemplateView):
    template_name = 'inventory/index.html'


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = MainInventory.objects.filter(user=self.request.user.id).order_by('id')

        low_inventory = MainInventory.objects.filter(
            user=self.request.user.id,
            quantity__lte=settings.LOW_QUANTITY
        )
        if low_inventory.count() > 0:
            if low_inventory.count() > 1:
                messages.error(request, f'{low_inventory.count()} items have low inventory')
            else:
                messages.error(request, f'{low_inventory.count()} item has low inventory')
        
        low_inventory_ids = MainInventory.objects.filter(
            user=self.request.user.id,
            quantity__lte=settings.LOW_QUANTITY
        ).values_list('id', flat=True)

        return render(request, 'inventory/dashboard.html', {'items': items, 'low_inventory_ids': low_inventory_ids})


class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            
            login(request, user)
            return redirect('index')
        
        return render(request, 'inventory/signup.html', {'form': form})
    

class AddItem(LoginRequiredMixin, CreateView):
    model = MainInventory
    form_class = MainInventoryForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class EditItem(LoginRequiredMixin, UpdateView):
    model = MainInventory
    form_class = MainInventoryForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('dashboard')


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = MainInventory
    template_name = 'inventory/delete_item.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'item'

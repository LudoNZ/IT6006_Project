from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import CustomUser
# Create your views here.
from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class AgentPageView(ListView):
    model = CustomUser
    template_name = "pages/agents.html"

class AgentDetailPageView(DetailView):
    model = CustomUser
    template_name = "pages/agentview.html"
    context_object_name = 'agentinfo'

class AgentUpdatePageView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "pages/agentedit.html"
    success_url="/agents"
    fields =["username", "age"]
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages
from .models import Song
from .forms import SongForm, LoginForm, RegisterForm
from django.contrib.auth.views import LoginView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def index(request):
    return redirect('songs')

def normalize_email(email):
    try:
        validate_email(email)
        return email.lower()
    except ValidationError:
        return None

class SongListView(ListView):
    model = Song
    context_object_name = "songs"
    template_name = "musicApp/song_list.html"


class SongDetailView(DetailView):
    model = Song
    template_name = "musicApp/song_detail.html"


class SongCreateView(LoginRequiredMixin, CreateView):
    model = Song
    form_class = SongForm
    template_name = "musicApp/song_form.html"


class SongUpdateView(LoginRequiredMixin, UpdateView):
    model = Song
    form_class = SongForm
    template_name = "musicApp/song_form.html"


class SongDeleteView(LoginRequiredMixin, DeleteView):
    model = Song
    template_name = "musicApp/song_confirm_delete.html"
    success_url = "/songs/"


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "musicApp/login.html"
    success_url = "/songs/"


class RegisterView(FormView):
    model = get_user_model()
    form_class = RegisterForm
    template_name = "musicApp/register.html"
    success_url = "/songs/"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponse("You are already logged in.")
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        email = normalize_email(form.cleaned_data.get('email'))  # Normalize the email
        password = form.cleaned_data.get('password1')
        user = get_user_model().objects.create_user(email=email, password=password) 
        login(self.request, user)
        return redirect('/')

    def form_invalid(self, form):
        # Handle form errors
        for errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)


class AboutView(TemplateView):
    template_name = "musicApp/about.html"

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomRegisterForm
from .models import CustomUser
class RegisterView(CreateView):
    #form_class = UserCreationForm
    form_class = CustomRegisterForm
    success_url = '/'
    template_name = 'users/register.html'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:user_list')

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'users/user_list.html'
    queryset = CustomUser.objects.all()

    def get_queryset(self):
        return self.queryset
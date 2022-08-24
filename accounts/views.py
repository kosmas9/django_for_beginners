from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    # redirect user upon successful registration
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Create your views here.

from django.views import generic
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.models import User

# User = get_user_model()

# Create your views here.html
# class UserCreateView(generic.CreateView):
class LoginView(TemplateView):
    template_name = 'registration/login.html'
    # model = User
    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)
    # def get_success_url(self):
    #     return reverse("login")

class ProfilePage(TemplateView):
    template_name = "registration/profile.html"

class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = "registration/contacts.html"

    def about(request):
        return render(request, "contacts.html", {'title': 'О магазине'})
from django.shortcuts import render, redirect
from accounts.forms import ManagerRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            form.save() # Manager will get stored into database
            messages.success(request, f'Account Created Successfully \for user {username} !!!')
            return redirect('login')
    else:
        form = ManagerRegistrationForm()
    return render(request, 'register.html', {'form': form})


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'
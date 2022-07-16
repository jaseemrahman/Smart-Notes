from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    dict_date={
        'today':datetime.today()
    }
    return render(request,'home/home.html',dict_date)

class LoginInterfaceView(LoginView):
    template_name='home/login.html'

class SignupView(CreateView):
    form_class=UserCreationForm
    template_name='home/signup.html' 
    success_url="notes"

    def get(self, request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name='home/logout.html'    

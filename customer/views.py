from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accs/login/')
def dashboard(request):
    return render(request,'customer/dashboard.html')
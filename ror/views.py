from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def login_page(request):

    print request.method
    if request.method == 'POST':
        return redirect('/home')
        
    return render(request, 'login.html')
    
    
        
def home_page(request):
    return render(request, 'home.html')
    

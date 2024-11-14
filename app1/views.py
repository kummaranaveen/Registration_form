from django.shortcuts import render, redirect
from .forms import LoginAttemptForm

def login_attempt(request):
    if request.method == 'POST':
        form = LoginAttemptForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('success_page') 
    else:
        form = LoginAttemptForm()

    return render(request, 'login.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

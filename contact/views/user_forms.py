from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from contact.forms import RegisterForm, LoginForm, RegisterUpdateForm
from contact.models import Contact
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def registerUser(request):
    form = RegisterForm()
    
    # messages.info(request, 'Um texto qualquer')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')
    
    return render(
        request,
        'contact/registerUser.html',
        {
            'form': form,
        }
    )

@login_required(login_url='contact:login')
def userUpdate(request):
    form = RegisterUpdateForm(instance=request.user)
    
    if request.method != 'POST':
    
        return render(
            request,
            'contact/updateUser.html',
            {
                'form': form
            }
        )
    form = RegisterUpdateForm(data=request.POST, instance=request.user)    
    if not form.is_valid():
        return render(
            request,
            'contact/updateUser.html',
            {
                'form': form
            }
        )
    form.save()
    return redirect('contact:userUpdate')
        
def userLogin(request):
    form = LoginForm(request)
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Login feito com sucesso')
            auth.login(request, user)
            return redirect('contact:index')
        messages.error(request, 'Login inválido')
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def userLogout(request):
    auth.logout(request)
    return redirect(
        'contact:login'
    )
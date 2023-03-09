from . import forms
from .forms import LoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from  django.views.decorators.cache import cache_control 
User = get_user_model()
from  django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404



def login_user(request):
    #crée une instance du formulaire
    form = forms.LoginForm()
    #definir une variable message pour informer le user si ses identifiant sont iccorecte
    message = ''
    #Test l'action si post (envoi de donnée)
    if request.method == 'POST':
        # On recupère les données dans l'instance du formulaire
        form = forms.LoginForm(request.POST)
        #Verifie si le formulaire est valide
        if form.is_valid():
            #On authentifie l'instance du user avec la methode authenticate
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            #Test si le usernme  envoyé du fomrulair ,'est pas null
            if user is not None:
                #Etablie une connection de lutilisateur
                login(request, user)
                #On le redirige vers une page ici c'est index.html
                return redirect('index')
            #si le formulaire n'est pas correct e.i si des les données dont incorrecte informé le user
        message = 'Invalide! verifiez votre nom d\'utilisateur ou votre mot de passe'
    return render(request, 'athentication/login_user.html', context={'form': form, 'message': message})



def logout_user(request):
    #deconnection du user avec la methode logout 
    logout(request)
    return redirect('login_user')


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Votre mot à été changé avec succès')
            return redirect('index')
        else:
            messages.error(request, 'Erreur veuillez verifiez vos identifiants antérieurs')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'athentication/change_password.html', {
        'form': form
    })
    
    
    
#Function to create users
def add_user(request):
    form = forms.CreateUser()
    if request.method == 'POST':
        form = forms.CreateUser(request.POST,request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'authentication/add.html', context={'form':form})

# Edit user edit function
def edit_user(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CreateUser(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save(id)
            return redirect('list')
    else:
        form = forms.CreateUser(instance=user)
    return render(request, 'authentication/edit.html', {'form':form})



def delete_user(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('list')
    return render(request, 'authentication/delete.html', {'user':user})

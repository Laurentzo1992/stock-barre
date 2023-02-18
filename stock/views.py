from . import forms
from .forms import ProductForm, LoginForm, Niveau1Form, Niveau2Form, Niveau3Form, Niveau4Form, Niveau5Form
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
User = get_user_model()
from  django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, FileResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Count, Sum
from stock.models import *
from escpos.printer import Usb



@login_required
def index(request):
    articles = Product.objects.all().count()
    context={"articles":articles}
    return render(request, 'stock/index.html', context)


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
        message = 'Invalides veuillez verifiez votre nom d\'utilisateur ou votre mot de passe'
    return render(request, 'stock/login_user.html', context={'form': form, 'message': message})



def logout_user(request):
    #deconnection du user avec la methode logout 
    logout(request)
    return redirect('login_user')


@login_required
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
    return render(request, 'stock/change_password.html', {
        'form': form
    })
    

@login_required
def niveau(request):
    return render(request, 'stock/niveau.html')

@login_required
def create_n1(request):
    niveau1 = Niveau1.objects.all()
    if request.method == 'POST':
        form = Niveau1Form(request.POST)
        if form.is_valid():
            form.save()
            cont_type = form.cleaned_data.get('name')
            messages.success(request, f"{cont_type} ajouté avec succès!")
            return HttpResponseRedirect('create_n1')
        else:
            messages.error(request, "Veuillez verifiez svpla saisie!")
            return render(request, 'stock/create_n1.html', {"niveau1":niveau1, 'form':form})
    else:
        form = Niveau1Form()
    return render(request, 'stock/create_n1.html', {"niveau1":niveau1, 'form':form})


@login_required
def create_n2(request):
    niveau2 = Niveau2.objects.all()
    if request.method == 'POST':
        form = Niveau2Form(request.POST)
        if form.is_valid():
            form.save()
            cont_type = form.cleaned_data.get('name')
            messages.success(request, f"{cont_type} ajouté avec succès!")
            return HttpResponseRedirect('create_n2')
        else:
            messages.error(request, "Veuillez verifiez svpla saisie!")
            return render(request, 'stock/create_n2.html', {"niveau2":niveau2, 'form':form})
    else:
        form = Niveau2Form()
    return render(request, 'stock/create_n2.html', {"niveau2":niveau2, 'form':form})

@login_required
def create_n3(request):
    niveau3 = Niveau3.objects.all()
    if request.method == 'POST':
        form = Niveau3Form(request.POST)
        if form.is_valid():
            form.save()
            cont_type = form.cleaned_data.get('name')
            messages.success(request, f"{cont_type} ajouté avec succès!")
            return HttpResponseRedirect('create_n3')
        else:
            messages.error(request, "Veuillez verifiez svpla saisie!")
            return render(request, 'stock/create_n3.html', {"niveau3":niveau3, 'form':form})
    else:
        form = Niveau3Form()
    return render(request, 'stock/create_n3.html', {"niveau3":niveau3, 'form':form})

@login_required
def create_n4(request):
    niveau4 = Niveau4.objects.all()
    if request.method == 'POST':
        form = Niveau4Form(request.POST)
        if form.is_valid():
            form.save()
            cont_type = form.cleaned_data.get('name')
            messages.success(request, f"{cont_type} ajouté avec succès!")
            return HttpResponseRedirect('create_n4')
        else:
            messages.error(request, "Veuillez verifiez svpla saisie!")
            return render(request, 'stock/create_n4.html', {"niveau4":niveau4, 'form':form})
    else:
        form = Niveau4Form()
    return render(request, 'stock/create_n4.html', {"niveau4":niveau4, 'form':form})

@login_required
def create_n5(request):
    niveau5 = Niveau5.objects.all()
    if request.method == 'POST':
        form = Niveau5Form(request.POST)
        if form.is_valid():
            form.save()
            cont_type = form.cleaned_data.get('name')
            messages.success(request, f"{cont_type} ajouté avec succès!")
            return HttpResponseRedirect('create_n5')
        else:
            messages.error(request, "Veuillez verifiez svpla saisie!")
            return render(request, 'stock/create_n5.html', {"niveau5":niveau5, 'form':form})
    else:
        form = Niveau5Form()
    return render(request, 'stock/create_n5.html', {"niveau5":niveau5, 'form':form})

@login_required
def commande(request):
    return render(request, 'stock/commande.html')

@login_required
def livraison(request):
    return render(request, 'stock/livraison.html')


@login_required
def produit(request):
    articles = Product.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request, 'stock/produit.html', context)


@login_required
def add_product(request):
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            pro_code = form.cleaned_data.get('code')
            nom_pro = form.cleaned_data.get('name')
            messages.success(request, f"L'élément {nom_pro} code {pro_code}  ajouté avec succes !")
            return HttpResponseRedirect('produit')
        else:
            messages.error(request, "Veuillez verifiez svp l'article existe déja!!")
            return render(request, 'stock/add_product.html', {"form":form})
    else:
        form = ProductForm()
        return render(request, 'stock/add_product.html', {"form":form})
    
@login_required   
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Mise à jour {product.code} ok !")
            return redirect('produit')
    else:
        form = ProductForm(instance=product)
    return render(request, 'stock/edit_product.html', {'form':form})


@login_required 
def delete_product(request, id):
    product = Product.objects.get(id=id)
    if request.method=='POST':
        product.delete()
        messages.success(request, f'{product.code} supprimé !')
        return redirect("produit")
    return render(request, 'stock/delete_product.html', {"product":product})

    
@login_required 
def suivi(request):
    return render(request, 'stock/suivi.html')


@login_required
def generate_barcode(product_number):
    #Crée un objet de code-barres Code128
    barcode = Code128(product_number)
    #Renvoie les données de code-barres en format binaire
    return barcode.get_barcode()



@login_required
def print_label(product):
    #Crée un objet d'imprimante USB
    printer = Usb(0x0416, 0x5011, 0, profile="POS-5890")
    #Configure l'imprimante pour une étiquette de 50 mm de largeur
    printer.set("CENTER")
    printer.set("SIZE", 1, 1)
    printer.set("GAP", 2)
    #Imprime le nom du produit
    printer.text(product.name + "\n")
    #Génère le code-barres et l'imprime
    barcode_data = generate_barcode(product.number)
    printer.barcode(barcode_data, "CODE128", 64, 2, '', '')
    #Imprime le numéro de produit et la quantité
    printer.text("Product number: " + product.number + "\n")
    printer.text("Quantity: " + str(product.quantity) + "\n")
    #Coupe le papier pour terminer l'étiquette
    printer.cut()
    #Ferme l'objet d'imprimante USB
    printer.close()
    return HttpResponse("Label printed successfully.")
    


@login_required
def product_label(request, product_id):
    #Récupère l'objet Produit correspondant à l'ID donné
    product = Product.objects.get(pk=product_id)
    #Imprime une étiquette pour le produit
    print_label(product)
    #Redirige l'utilisateur vers la page de détails du produit
    return redirect('product_detail', product_id=product_id)


    

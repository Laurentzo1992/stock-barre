from django.db import models
import barcode
from barcode import Code128
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from phonenumber_field.modelfields import PhoneNumberField
import datetime



class Niveau1(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Niveau 1")
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.name
    
    
class Niveau2(models.Model):
    name = models.CharField(max_length=100)
    niveau1 = models.ForeignKey(Niveau1, null=True, blank=True, verbose_name="Niveau 2", on_delete=models.CASCADE, related_name='niveau2')
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Niveau3(models.Model):
    name = models.CharField(max_length=100)
    niveau2 = models.ForeignKey(Niveau2, null=True, blank=True, verbose_name="Niveau 3", on_delete=models.CASCADE, related_name='niveau3')
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Niveau4(models.Model):
    name = models.CharField(max_length=100)
    niveau3 = models.ForeignKey(Niveau3, null=True, blank=True, verbose_name="Niveau 4", on_delete=models.CASCADE, related_name='niveau4')
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    

class Niveau5(models.Model):
    name = models.CharField(max_length=100)
    niveau4 = models.ForeignKey(Niveau4, null=True, blank=True, verbose_name="Niveau 5", on_delete=models.CASCADE, related_name='niveau5')
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.name
    


class Client(models.Model):
    rasion_sociale = models.CharField(max_length=100, null=True, blank=True)
    nom_prenom = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True, verbose_name="Numero de téléphone")
    email = models.EmailField(null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.rasion_sociale
    
    
class Transporteur(models.Model):
    name_transp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nom entreprise")
    coordonn1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="coordonnée 1")
    coordonn2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="coordonnée 2")
    type_trans = models.CharField(max_length=100, null=True, blank=True, verbose_name="Type de livraison")
    phone_number = PhoneNumberField(unique=True, null=True, blank=True, verbose_name="Numero de téléphone")
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name_transp
    
class Product(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    stock = models.IntegerField()
    sous_contenaire = models.ForeignKey(Niveau5, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()
    barcode = models.FileField(upload_to='barcode', blank=True)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)
    

    def __str__(self):
            return self.name
    
    
    def save(self, *args, **kwargs):
        Code128 = barcode.get_barcode_class('Code128')
        ean = Code128(f'{self.code}-{self.sous_contenaire.name}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.name}{self.code}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)



class Operation(models.Model):
    products = models.ManyToManyField(Product, through='LigneOperation')
    fournisseur = models.ForeignKey(Client, verbose_name='Fournisseur', on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.product.name
    


class LigneOperation(models.Model):
    product = models.ForeignKey(Product, verbose_name='produit', on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.product.code
    
class Commande(models.Model):
    num_commande = models.CharField(unique=True, max_length=100, null=True, blank=True)
    articles = models.ManyToManyField(Product, through='LigneCommande')
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    date_commande = models.DateField(null=True, blank=True)
    adresse_livraison = models.TextField(null=True, blank=True)
    transport = models.ForeignKey(Transporteur, null=True, blank=True, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.num_commande
    
    
class LigneCommande(models.Model):
    article = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, null=True, blank=True, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)


class Livraison(models.Model):
    num_livraison = models.CharField(unique=True, max_length=100, null=True, blank=True)
    commande = models.ForeignKey(Commande, null=True, blank=True, on_delete=models.CASCADE)
    date_livaison = models.DateField(null=True, blank=True)
    livre = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.num_livraison
    
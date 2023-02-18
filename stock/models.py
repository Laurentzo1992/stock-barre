from django.db import models
import barcode
from barcode import Code128
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File



class Niveau1(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Niveau 1")

    def __str__(self):
        return self.name
    
    
class Niveau2(models.Model):
    name = models.CharField(max_length=100)
    niveau1 = models.ForeignKey(Niveau1, null=True, blank=True, verbose_name="Niveau 2", on_delete=models.CASCADE, related_name='niveau2')


    def __str__(self):
        return self.name
    
    
class Niveau3(models.Model):
    name = models.CharField(max_length=100)
    niveau2 = models.ForeignKey(Niveau2, null=True, blank=True, verbose_name="Niveau 3", on_delete=models.CASCADE, related_name='niveau3')


    def __str__(self):
        return self.name
    
    
class Niveau4(models.Model):
    name = models.CharField(max_length=100)
    niveau3 = models.ForeignKey(Niveau3, null=True, blank=True, verbose_name="Niveau 4", on_delete=models.CASCADE, related_name='niveau4')


    def __str__(self):
        return self.name
    
    

class Niveau5(models.Model):
    name = models.CharField(max_length=100)
    niveau4 = models.ForeignKey(Niveau4, null=True, blank=True, verbose_name="Niveau 5", on_delete=models.CASCADE, related_name='niveau5')


    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    stock = models.IntegerField()
    sous_contenaire = models.ForeignKey(Niveau5, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()
    barcode = models.FileField(upload_to='barcode', blank=True)
    

    def __str__(self):
            return self.name
    
    
    def save(self, *args, **kwargs):
        Code128 = barcode.get_barcode_class('Code128')
        ean = Code128(f'{self.code}{self.name}{self.sous_contenaire.name}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.name}{self.code}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)



class Client(models.Model):
    rasion_sociale = models.CharField(max_length=100, null=True, blank=True)
    nom_prenom = models.CharField(max_length=10, null=True, blank=True)
    adresse = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"self.rasion_sociale +" " + self.nom_prenom"
    
    
class Transporteur(models.Model):
    name_transp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nom entreprise")
    coordonn = models.CharField(max_length=100, null=True, blank=True, verbose_name="coordonnées")
    type_trans = models.CharField(max_length=100, null=True, blank=True, verbose_name="Type de livraison")
    
    def __str__(self):
        return self.name_transp
    
    
    
class Commande(models.Model):
    status = (
        ('pending', 'en cours de traitement'),
        ('expeded', 'expédiée'),
        ('cancel', 'annulée'),
    )
    num_commande = models.CharField(max_length=100, null=True, blank=True)
    article = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    paye = models.BooleanField(default=False)
    status = models.CharField(max_length=100, null=True, blank=True, choices=status)

    def __str__(self):
        return self.num_commande
    

    
class Suivi(models.Model):
    status = (
        ('transit', 'en transit'),
        ('ok', 'livré'),
    )
    num_suivi = models.CharField(max_length=100, null=True, blank=True)
    commande = models.ForeignKey(Commande, null=True, blank=True, on_delete=models.CASCADE)
    transporteur  = models.ForeignKey(Transporteur, null=True, blank=True, on_delete=models.CASCADE)
    date_expedition = models.DateTimeField()
    status = models.CharField(max_length=100, null=True, blank=True, choices=status)

    def __str__(self):
        return self.num_suivi
    

class Livraison(models.Model):
    name_dest = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nom et Prenom du destinataire")
    num_livraison = models.CharField(max_length=100, null=True, blank=True)
    commande = models.ForeignKey(Commande, null=True, blank=True, on_delete=models.CASCADE)
    date_livaison = models.DateTimeField(auto_now_add=True)
    livre = models.BooleanField(default=False)


    def __str__(self):
        return self.num_livraison
# Generated by Django 4.1.7 on 2023-03-09 12:24

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rasion_sociale",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("nom_prenom", models.CharField(blank=True, max_length=10, null=True)),
                ("adresse", models.TextField(blank=True, null=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        unique=True,
                        verbose_name="Numero de téléphone",
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Commande",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "num_commande",
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                ("date_commande", models.DateField(blank=True, null=True)),
                ("adresse_livraison", models.TextField(blank=True, null=True)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="LigneOperation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Niveau1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Niveau 1"
                    ),
                ),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Niveau2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                (
                    "niveau1",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="niveau2",
                        to="stock.niveau1",
                        verbose_name="Niveau 2",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Niveau3",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                (
                    "niveau2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="niveau3",
                        to="stock.niveau2",
                        verbose_name="Niveau 3",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Niveau4",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                (
                    "niveau3",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="niveau4",
                        to="stock.niveau3",
                        verbose_name="Niveau 4",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Niveau5",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                (
                    "niveau4",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="niveau5",
                        to="stock.niveau4",
                        verbose_name="Niveau 5",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transporteur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_transp",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Nom entreprise",
                    ),
                ),
                (
                    "coordonn1",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="coordonnée 1",
                    ),
                ),
                (
                    "coordonn2",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="coordonnée 2",
                    ),
                ),
                (
                    "type_trans",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Type de livraison",
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        unique=True,
                        verbose_name="Numero de téléphone",
                    ),
                ),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("stock", models.IntegerField()),
                ("description", models.TextField()),
                ("barcode", models.FileField(blank=True, upload_to="barcode")),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                (
                    "sous_contenaire",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stock.niveau5",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Operation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                (
                    "fournisseur",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stock.client",
                        verbose_name="Fournisseur",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        through="stock.LigneOperation", to="stock.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Livraison",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "num_livraison",
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                ("date_livaison", models.DateField(blank=True, null=True)),
                ("livre", models.BooleanField(default=False)),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                (
                    "commande",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stock.commande",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="ligneoperation",
            name="operation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stock.operation",
            ),
        ),
        migrations.AddField(
            model_name="ligneoperation",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="stock.product",
                verbose_name="produit",
            ),
        ),
        migrations.CreateModel(
            name="LigneCommande",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantite", models.PositiveIntegerField()),
                ("create_at", models.DateField(auto_now_add=True, null=True)),
                (
                    "article",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stock.product",
                    ),
                ),
                (
                    "commande",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stock.commande",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="commande",
            name="articles",
            field=models.ManyToManyField(
                through="stock.LigneCommande", to="stock.product"
            ),
        ),
        migrations.AddField(
            model_name="commande",
            name="client",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stock.client",
            ),
        ),
        migrations.AddField(
            model_name="commande",
            name="transport",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stock.transporteur",
            ),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-17 13:23

from django.db import migrations, models
import django.db.models.deletion


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
                ("adresse", models.CharField(blank=True, max_length=100, null=True)),
                ("telephone", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
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
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("date_commande", models.DateTimeField(auto_now_add=True)),
                ("paye", models.BooleanField(default=False)),
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
                ("name", models.CharField(max_length=100)),
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
                (
                    "niveau1",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="niveau2",
                        to="stock.niveau1",
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
                (
                    "niveau2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="niveau3",
                        to="stock.niveau2",
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
                (
                    "niveau3",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="niveau4",
                        to="stock.niveau3",
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
                (
                    "niveau4",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="niveau5",
                        to="stock.niveau4",
                    ),
                ),
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
                ("code", models.CharField(blank=True, max_length=100, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("stock", models.IntegerField()),
                ("description", models.TextField()),
                ("barcode", models.FileField(blank=True, upload_to="barcode")),
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
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("date_livaison", models.DateTimeField(auto_now_add=True)),
                ("livre", models.BooleanField(default=False)),
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
            name="article",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stock.product",
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
    ]

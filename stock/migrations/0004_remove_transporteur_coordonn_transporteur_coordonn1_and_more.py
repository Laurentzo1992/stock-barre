# Generated by Django 4.1.7 on 2023-02-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0003_commande_transport"),
    ]

    operations = [
        migrations.RemoveField(model_name="transporteur", name="coordonn",),
        migrations.AddField(
            model_name="transporteur",
            name="coordonn1",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="coordonnée 1"
            ),
        ),
        migrations.AddField(
            model_name="transporteur",
            name="coordonn2",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="coordonnée 2"
            ),
        ),
    ]
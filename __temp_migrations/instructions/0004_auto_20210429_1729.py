# Generated by Django 2.2.12 on 2021-04-29 15:29

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0003_auto_20210429_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='answerQ1',
            field=otree.db.models.FloatField(null=True, verbose_name='Quel est votre gain si vous achetez le quatrième produit ?'),
        ),
    ]
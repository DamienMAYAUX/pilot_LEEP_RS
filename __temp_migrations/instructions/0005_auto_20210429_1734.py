# Generated by Django 2.2.12 on 2021-04-29 15:34

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0004_auto_20210429_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='answerQ5',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name="Si à deux étapes différentes j'ai le choix entre exactement les mêmes produits, est-ce que la recommandation sera deux fois la même ?"),
        ),
    ]
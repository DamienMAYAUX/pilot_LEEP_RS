# Generated by Django 2.2.12 on 2021-04-29 16:09

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('conclusion', '0005_auto_20210429_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='feedback',
            field=otree.db.models.LongStringField(null=True, verbose_name="N'hésitez pas à donner ci-dessous votre ressenti                                      sur l'expérience,\n à expliquer comment vous avez procédé ou à                                          partager vos intuitions\n sur la pertinence de la recommandation."),
        ),
    ]
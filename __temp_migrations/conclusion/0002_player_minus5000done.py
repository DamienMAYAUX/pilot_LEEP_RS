# Generated by Django 2.2.12 on 2021-05-23 08:22

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('conclusion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='minus5000done',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
    ]

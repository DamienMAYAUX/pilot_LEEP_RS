# Generated by Django 2.2.12 on 2021-06-23 20:58

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions_group', to='otree.Session')),
            ],
            options={
                'db_table': 'instructions_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructions_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'instructions_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('genre', otree.db.models.StringField(choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Autre', 'Autre')], max_length=10000, null=True)),
                ('age', otree.db.models.StringField(choices=[('15-17 ans', '15-17 ans'), ('18-24 ans', '18-24 ans'), ('25-34 ans', '25-34 ans'), (' 35-49 ans', ' 35-49 ans'), ('50-64 ans', '50-64 ans'), ('Plus de 65 ans', 'Plus de 65 ans')], max_length=10000, null=True)),
                ('etudes', otree.db.models.StringField(choices=[('Sans diplôme', 'Sans diplôme'), ('Brevet des collèges, BEPC', 'Brevet des collèges, BEPC'), ('CAP, BEP', 'CAP, BEP'), ('Baccalaureat', 'Baccalaureat'), ('Bac +2 (DUT, BTS, DEUG)', 'Bac +2 (DUT, BTS, DEUG)'), ("Diplôme de l'enseignement supérieur", "Diplôme de l'enseignement supérieur")], max_length=10000, null=True)),
                ('answerQ1', otree.db.models.FloatField(null=True, verbose_name='Quel est votre gain si vous achetez le quatrième produit ?')),
                ('answerQ2', otree.db.models.FloatField(null=True, verbose_name="Quel est le gain le plus élevé que vous puissiez obtenir avec l'un des produits disponibles ?")),
                ('answerQ3', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name="Y a-t-il une relation entre l'ordre dans lequel les produits apparaissent à l'écran et la recommandation ?")),
                ('answerQ4', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name="A la première étape, la recommandation était vraiment mauvaise. Est-ce que cela veut dire qu'elle le sera également à toutes les étapes suivantes ?")),
                ('answerQ5', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name="Si à deux étapes différentes j'ai le choix entre exactement les mêmes produits, est-ce que la recommandation sera deux fois la même ?")),
                ('correctQ1', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('correctQ2', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('correctQ3', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('correctQ4', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('correctQ5', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instructions.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructions.Subsession')),
            ],
            options={
                'db_table': 'instructions_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructions.Subsession'),
        ),
    ]

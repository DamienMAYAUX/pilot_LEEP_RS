from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import csv


class PlayerBot(Bot):
    def play_round(self):
        
        with open('trial_set_FR.csv', newline='', encoding='cp1252') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            for row in csv_reader:
                if row['round'] == str(self.round_number) \
                    and ( float(row['total_points']) < 0 \
                         or row['bad_rec'] == "TRUE"):
                    choice_value = row['order']
                    break 
        
        #choice_value = 1
        
        yield pages.WaitPage_FR
        yield pages.ChoiceRound_FR, dict(choice = choice_value)

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random


author = 'Damien Mayaux'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'choice_experiment'
    players_per_group = None
    num_rounds = 10
    num_products = 6
    seed = 13


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    #information_quality = models.IntegerField()
    #round_order = models.IntegerField()
    pass


class Player(BasePlayer):
    choice = models.IntegerField(choices = [1,2,3,4,5,6])
    timeout_reached = models.BooleanField(initial = False)
    
    
    
    #label1 = 1
    #nutrition1 = 2
    #price1 = 5

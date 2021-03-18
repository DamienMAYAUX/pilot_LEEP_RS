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


author = 'Damien Mayaux'

doc = """
This short break in the middle of the game allows me to test the particpant's attention'
"""


class Constants(BaseConstants):
    name_in_url = 'attention_test'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    feedback = models.LongStringField(label = "Feel free to leave us a feedback on the experiment ")

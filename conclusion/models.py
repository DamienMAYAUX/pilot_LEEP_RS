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
    # feedback = models.LongStringField(label = "Feel free to leave us a feedback on the experiment ")
    feedback = models.LongStringField( label = """N'hésitez pas à donner ci-dessous votre ressenti\
                                      sur l'expérience,\n à expliquer comment vous avez procédé ou à\
                                          partager vos intuitions\n sur la pertinence de la recommandation.""")
    minus5000done = models.BooleanField(initial=False)
        
        
        
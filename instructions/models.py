from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range
)

author = 'Damien Mayaux'

doc = """
This initial part introduces the game and tests the understanding of the rules
"""

class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1
    num_choice_rounds = 20
    language = "English"
    #language = "French"
    num_products = 6
    

class Subsession(BaseSubsession):
    def creating_session(self):
        import itertools
        information_level = itertools.cycle([0,1,2,3,4,5])
        first_trials_order = itertools.cycle([0,1,2])
        for player in self.get_players():
            player.participant.vars['information_quality'] = next(information_level)
            player.participant.vars['first_trials_order'] = next(first_trials_order)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    name = models.StringField()
    gender = models.StringField(choices = ['Homme','Femme','Autre'])
    age = models.IntegerField()
    
    answerQ1 = models.FloatField(label = 'What is your payoff when buying the forth product ?')    
    answerQ2 = models.FloatField(label = 'What is the highest payoff you can get from one of the available products ?')       
    
    answerQ3 = models.BooleanField(label = 'Is there a relation between the order in which the product appear on the screen and the recommandation ?')  
    answerQ4 = models.BooleanField(label = 'In the first round, the recommandation was very bad. Does it mean that it will always be so ?')    
    answerQ5 = models.BooleanField(label = 'If I face the same 6 products at two differents rounds, will I receive the same recommandation ?')  
    
    
    
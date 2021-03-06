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
    num_choice_rounds = 30
    #language = "English"
    language = "French"
    num_products = 6
    

class Subsession(BaseSubsession):
    def creating_session(self):
        import itertools
        #information_level = itertools.cycle([0,1,2,3,4])
        information_level = itertools.cycle([4,0,3,2,1])
        #first_trials_order = itertools.cycle([0,1,2])
        for player in self.get_players():
            player.participant.vars['information_quality'] = next(information_level)
            #player.participant.vars['first_trials_order'] = next(first_trials_order)
            player.participant.vars['first_trials_order'] = 0

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    
    ## English version
    
    # gender = models.StringField(choices = ['Homme','Femme','Autre'])
    # name = models.StringField()
    # age = models.IntegerField()
    
    # answerQ1 = models.FloatField(label = 'What is your payoff when buying the forth product ?')    
    # answerQ2 = models.FloatField(label = 'What is the highest payoff you can get from one of the available products ?')       
    
    # answerQ3 = models.BooleanField(label = 'Is there a relation between the order in which the product appear on the screen and the recommandation ?')  
    # answerQ4 = models.BooleanField(label = 'In the first round, the recommandation was very bad. Does it mean that it will always be so ?')    
    # answerQ5 = models.BooleanField(label = 'If I face the same 6 products at two differents rounds, will I receive the same recommandation ?')  
    
    ## French version
    
    genre = models.StringField(choices = ['Homme','Femme','Autre'])
    age = models.StringField(choices = ['15-17 ans','18-24 ans','25-34 ans',' 35-49 ans', '50-64 ans', 'Plus de 65 ans'])
    etudes = models.StringField(choices = ['Sans dipl??me', 'Brevet des coll??ges, BEPC','CAP, BEP','Baccalaureat', 'Bac +2 (DUT, BTS, DEUG)', 'Dipl??me de l\'enseignement sup??rieur'])
    
    
    answerQ1 = models.FloatField(label = 'Quel est votre gain si vous achetez le quatri??me produit ?')    
    answerQ2 = models.FloatField(label = 'Quel est le gain le plus ??lev?? que vous puissiez obtenir avec l\'un des produits disponibles ?')       
    
    answerQ3 = models.BooleanField(label = 'Y a-t-il une relation entre l\'ordre dans lequel les produits apparaissent ?? l\'??cran et la recommandation ?')  
    answerQ4 = models.BooleanField(label = 'A la premi??re ??tape, la recommandation ??tait vraiment mauvaise. Est-ce que cela veut dire qu\'elle le sera ??galement ?? toutes les ??tapes suivantes ?')    
    answerQ5 = models.BooleanField(label = 'Si ?? deux ??tapes diff??rentes j\'ai le choix entre exactement les m??mes produits, est-ce que la recommandation sera deux fois la m??me ?')  
    
    correctQ1 = models.BooleanField(initial=True)
    correctQ2 = models.BooleanField(initial=True)
    correctQ3 = models.BooleanField(initial=True)
    correctQ4 = models.BooleanField(initial=True)
    correctQ5 = models.BooleanField(initial=True)
    
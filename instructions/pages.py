from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Presentation_FR(Page):
    form_model = 'player'
    
    #form_fields = ['name', 'age', 'gender']
    form_fields = ['genre', 'age', 'etudes']

class Instructions1_FR(Page):
    form_model = 'player'
    form_fields = ['answerQ1', 'answerQ2']
    
    def answerQ1_error_message(player, value):
        if value != 2.12:
            player.participant.vars['correctQ1'] = False
            # return 'You should have found 2.12, computed as 2 (for label star) + 2 (for nutrition level D) - 1.88 (for the price)'
            return 'Vous auriez dû trouver 2.12, en comptant 2 (pour le label étoile) + 2 (pour la qualité nutritionnelle D) - 1.88 (pour le prix)'    
        
    def answerQ2_error_message(player, value):
        if value != 4.72:
            player.participant.vars['correctQ2'] = False
            # return "The payoff is below 1 ECU for the fifth product and negative for the sixth one. Thus, the best option is 4.72 ECU with the third product"
            return "Le gain est inférieur à 1 ECU pour le 5e produit et négatif pour le 6e. Le plus haut gain est donc 4.72 ECU avec le 3e produit"

class Instructions2_FR(Page):
    
    form_model = 'player'
    
    def get_form_fields(player):
        if player.participant.vars['information_quality'] > 0:
            return ['answerQ3', 'answerQ4', 'answerQ5']
        else:
            return []
        #form_fields = ['answerQ3', 'answerQ4', 'answerQ5']
    
    def answerQ3_error_message(player, value):
        if value:
            player.participant.vars['correctQ3'] = False
            # return "The answer is no. The recommandation depends only on the attributes of the available products"
            return "La réponse est non. La recommandation dépend seulement des caractéristiques des produits disponibles, c'est-à-dire le label, la qualité nutritionnelle et le prix"
        
    def answerQ4_error_message(player, value):
        if value:
            player.participant.vars['correctQ4'] = False
            # return "Not necessarly. The algorithm that determines the recommendation will not change during the experiment, but it may perform better in some situations than in others."
            return "Pas nécessairement. La façon dont la recommandation est déterminée ne change pas durant l\'expérience, mais elle peut être plus adaptée à certains ensembles de produits qu'à d'autres."
        
    def answerQ5_error_message(player, value):
        if not value:
            player.participant.vars['correctQ5'] = False
            # return "The answer is yes. The recommendation is determined only from the attributes of the available products"
            return "La réponse est oui. La recommandation est déterminée uniquement à partir des caractéristiques des produits, c'est-à-dire le label, la qualité nutritionnelle et le prix"
 
    def vars_for_template(self):
        return {'information_quality' : self.player.participant.vars['information_quality']}



page_sequence = [Presentation_FR, Instructions1_FR, Instructions2_FR]
#, InstructionsQuizz, ChoiceRound, Results]

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Presentation(Page):
    form_model = 'player'
    form_fields = ['name', 'age', 'gender']

class Instructions1(Page):
    
    form_model = 'player'
    form_fields = ['answerQ1', 'answerQ2']
    
    def answerQ1_error_message(player, value):
        if value != 2.12:
            player.participant.vars['correctQ1'] = False
            return 'You should have found 2.12 = 2 (for label star) + 2 (for nutrition level D) - 1.88 (for the price)'
        
    def answerQ2_error_message(player, value):
        if value != 4.72:
            player.participant.vars['correctQ2'] = False
            return "It is below 1 ECU for the fifth product and negative for the last one. Thus, the best option is 4.72 ECU with the third product"
        

class Instructions2(Page):
    
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
            return "The answer is no. The recommandation depends only on the attributes of the available products"
        
    def answerQ4_error_message(player, value):
        if value:
            player.participant.vars['correctQ4'] = False
            return "Not necessarly. The algorithm that determines the recommendation will not change during the experiment, but it may perform better in some situations than in others."
        
    def answerQ5_error_message(player, value):
        if not value:
            player.participant.vars['correctQ5'] = False
            return "The answer is yes. The recommendation is determined only from the attributes of the available products"
        
    def vars_for_template(self):
        return {'information_quality' : self.player.participant.vars['information_quality']}



page_sequence = [Presentation, Instructions1, Instructions2]
#, InstructionsQuizz, ChoiceRound, Results]

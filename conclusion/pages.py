from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class LastPage_FR(Page):
    form_model = 'player'
    form_fields = ['feedback']
    
    def vars_for_template(self):
        return {'payoff_normalized' : float(self.player.participant.payoff)/100}


page_sequence = [LastPage_FR]

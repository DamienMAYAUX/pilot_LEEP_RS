from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants,Player

class LastPage_FR(Page):
    form_model = 'player'
    form_fields = ['feedback']
    
    def vars_for_template(self):
        if not self.player.minus5000done:
            self.player.participant.payoff = max(self.player.participant.payoff - 5000,\
                                                 self.player.participant.payoff * 0)
            self.player.minus5000done=True
        return {'payoff_normalized' : float(self.player.participant.payoff + 5000)/100}

class RedirectPage_FR(Page):

    def vars_for_template(self):
        if not (not self.player.participant.label):
            from urllib.request import urlopen
            f = urlopen('https://s2ch.fr/expenligne/expe/DMayaux/connect.php?name='+str(self.player.participant.label)+'&ajax=1&status=setvarsgetlinkcode&Finished=1&gainEUR='+(str(self.player.participant.payoff_plus_participation_fee())).split(' ')[0].replace(',','.'))
            key=f.read().decode('utf-8')
        return {'redirect_page' : '' if not self.player.participant.label else 'https://s2ch.fr/expenligne/expe/DMayaux/paydistrib.php?name='+str(self.player.participant.label)+'&key='+key}


page_sequence = [LastPage_FR, RedirectPage_FR]

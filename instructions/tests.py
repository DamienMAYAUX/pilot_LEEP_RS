from otree.api import Currency as c, currency_range
from otree.api import Submission
from . import pages
from ._builtin import Bot
from .models import Constants



class PlayerBot(Bot):
    def play_round(self):
        yield pages.Presentation_FR, dict(etudes= 'Brevet des collèges, BEPC', age = '15-17 ans', genre = 'Autre')
        yield pages.Instructions1_FR, dict(answerQ1 = 2.12, answerQ2 = 4.72)
        if self.player.participant.vars['information_quality'] > 0:
            yield pages.Instructions2_FR, dict(answerQ3 = False, answerQ4 = False, answerQ5 = True)
        else:
            yield Submission(pages.Instructions2_FR, dict(answerQ3 = False, answerQ4 = False, answerQ5 = True), check_html=False)

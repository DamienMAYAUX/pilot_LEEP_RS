from otree.api import Currency as c, currency_range
from otree.api import Submission
from . import pages
from ._builtin import Bot
from .models import Constants



class PlayerBot(Bot):
    def play_round(self):
        yield pages.Presentation, dict(name = 'Joe', age = '12', gender = 'Autre')
        yield pages.Instructions1, dict(answerQ1 = 2.12, answerQ2 = 4.72)
        if self.player.participant.vars['information_quality'] > 0:
            yield pages.Instructions2, dict(answerQ3 = False, answerQ4 = False, answerQ5 = True)
        else:
            yield Submission(pages.Instructions2, dict(answerQ3 = False, answerQ4 = False, answerQ5 = True), check_html=False)

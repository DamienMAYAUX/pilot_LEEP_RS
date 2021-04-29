from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import csv

class ChoiceRound_FR(Page):
    
    form_model = 'player'
    form_fields = ['choice']
    
    # The second treatment consists in changing the order in which the first trials appear
    # This order must be :
    # - 1, 2, 3, 4, 5, 6 when first_trials_order == 0
    # - 3, 4, 5, 6, 1, 2 when first_trials_order == 1
    # - 5, 6, 1, 2, 3, 4 when first_trials_order == 2
    # The order of the trials above 7 included is not modified
    def current_trial_number(self):
        
            player = self.player
            base_trial_number = self.round_number
            
            if base_trial_number <= 6:
                return (base_trial_number + 2* player.participant.vars['first_trials_order'] - 1) % 6 + 1
            else:
                return base_trial_number
    
    
    def vars_for_template(self):        
        
        player = self.player
        with open('trial_set.csv', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',', )
            key_list, value_list = [], []
                       
            trial_number = self.current_trial_number()
            
            for row in csv_reader:
                if row['round'] == str(trial_number):
                    for variable_name in csv_reader.fieldnames:
                        if not (variable_name in ["", "order", "round"]):
                            key_list.append( variable_name + row['order'] )
                            if "rec" in variable_name:
                                value_list.append(row[variable_name] == "TRUE")
                            else:
                                value_list.append(row[variable_name])
        
        variable_dict = dict( zip(key_list,value_list) )
        variable_dict['information_quality'] = player.participant.vars['information_quality']
        #variable_dict = {'forloop' : [(3, "nutrition", "Blu", 5, "blo"), (2, "natation", "Blo", 3, "bla")]}

        return variable_dict
    
    
    timeout_seconds = 60
    
    def before_next_page(self):
        
        player = self.player
        trial_number = self.current_trial_number()
        
        # Determine the payoff of the player
        # IS IT POSSIBLE TO CALL VARS_FOR_TEMPLATE FROM HERE ?
        with open('trial_set.csv', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            for row in csv_reader:
                if row['round'] == str(trial_number) and row['order'] == str(player.choice):
                    player.payoff = 100*float(row['total_points'])
        
        # Check if the player has chosen a product or if the application has moved automatically to the next page
        # Store the answer in the player-specific boolean field 'did_not_play'
        timeout_happened = self.timeout_happened
        if timeout_happened:
            player.timeout_reached = True
            
          

page_sequence = [ChoiceRound_FR]
#, InstructionsQuizz, ChoiceRound, Results]

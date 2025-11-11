# EnvironmentC

import random
                                                                                                                                                                                                        
class EnvironmentC:
    
    # Everything external to the Agent


    def __init__(self, environment_name, data_file, rules_file):
        
        self.environment_name = environment_name
        self.data_file        = data_file
        self.rules_file       = rules_file


    def load_data(self) -> []:

        current_effectiveness_domain = ['great', 'good', 'okay', 'bad']
        operating_system_domain = ['great', 'good', 'okay', 'bad']
        risk_domain = ['great', 'good', 'okay', 'bad']
        cost_domain = ['great', 'good', 'okay', 'bad']

        data_list = []

        for i in range(5):

            app_name = "App" + str(i)
            ce_prob = [0.25, 0.25, 0.25, 0.25]
            os_prob = [0.30, 0.20, 0.40, 0.10]
            ri_prob = [0.20, 0.20, 0.10, 0.50]
            co_prob = [0.50, 0.25, 0.15, 0.10]

            ce_choice = random.choices(current_effectiveness_domain, weights=ce_prob, k=1)[0]
            os_choice = random.choices(operating_system_domain, weights=os_prob, k=1)[0]
            ri_choice = random.choices(risk_domain, weights=ri_prob, k=1)[0]
            co_choice = random.choices(cost_domain, weights=co_prob, k=1)[0]

            data_dict = ({ "APPLICATION" : app_name, 
                               "CURRENT_EFFECTIVENESS" : ce_choice,
                               "OPERATING_SYSTEM" : os_choice,
                               "RISK" : ri_choice,
                               "COST" : co_choice })
            data_list.append(data_dict)

        return data_list


    def display_output(self):

        pass







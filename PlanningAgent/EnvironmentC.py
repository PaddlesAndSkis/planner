# EnvironmentC

import random
                                                                                                                                                                                                        
class EnvironmentC:
    
    # Everything external to the Agent


    def __init__(self, environment_name, data_file, rules_file):
        
        self.environment_name = environment_name
        self.data_file        = data_file
        self.rules_file       = rules_file


    def load_data(self) -> []:
        
        client_satisfaction_domain = ['great', 'good', 'okay', 'bad']
        business_criticality_domain = ['yes' , 'no']
        software_technology_domain = ['excellent', 'good', 'okay', 'bad']
        hardware_technology_domain = ['excellent', 'good', 'okay', 'bad']
        user_experience_domain = ['positive', 'negative']
        risk_domain = ['great', 'good', 'okay', 'bad']
        cost_domain = ['great', 'good', 'okay', 'bad']

        data_list = []

        for i in range(5):

            app_name = "App" + str(i)
            cs_prob = [0.25, 0.25, 0.25, 0.25]
            bc_prob = [0.25, 0.75]
            st_prob = [0.30, 0.20, 0.40, 0.10]
            ue_prob = [0.60, 0.40]
            ri_prob = [0.20, 0.20, 0.10, 0.50]
            co_prob = [0.50, 0.25, 0.15, 0.10]

            cs_choice = random.choices(client_satisfaction_domain, weights=cs_prob, k=1)[0]
            bc_choice = random.choices(business_criticality_domain, weights=bc_prob, k=1)[0]
            st_choice = random.choices(software_technology_domain, weights=st_prob, k=1)[0]
            ht_choice = random.choices(hardware_technology_domain, weights=st_prob, k=1)[0]
            ue_choice = random.choices(user_experience_domain, weights=ue_prob, k=1)[0]
            ri_choice = random.choices(risk_domain, weights=ri_prob, k=1)[0]
            co_choice = random.choices(cost_domain, weights=co_prob, k=1)[0]

            number_users = random.randint(1, 3000)


            data_dict = ({ "APPLICATION" : app_name, 
                           "CLIENT_SATISFACTION" : cs_choice,
                           "BUSINESS_CRITICALITY" : bc_choice,
                           "NUMBER_USERS" : str(number_users),
                           "SOFTWARE_TECHNOLOGY" : st_choice,
                           "HARDWARE_TECHNOLOGY" : ht_choice,
                           "USER_EXPERIENCE" : ue_choice,
                           "RISK" : ri_choice,
                           "COST" : co_choice })
            data_list.append(data_dict)

        return data_list


    def display_output(self):

        pass







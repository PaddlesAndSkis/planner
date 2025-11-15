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

        executive_support_domain = ['excellent', 'good', 'okay', 'bad']
        resource_availability_domain = ['excellent', 'good', 'okay', 'bad']
        business_requirements_domain = ['excellent', 'good', 'okay', 'bad']

        hardware_maintenance_domain = ['high', 'medium', 'low']
        software_maintenance_domain = ['high', 'medium', 'low']
        funding_availability_domain = ['excellent', 'good', 'okay', 'bad']

        modern_architecture_domain = ['excellent', 'good', 'okay', 'bad']
        cloud_readiness_domain = ['ready', 'postpone']

        data_list = []

        for i in range(10):

            app_name = "App" + str(i)

            # Business Layer

            cs_prob = [0.25, 0.25, 0.25, 0.25]
            bc_prob = [0.25, 0.75]

            cs_choice = random.choices(client_satisfaction_domain, weights=cs_prob, k=1)[0]
            bc_choice = random.choices(business_criticality_domain, weights=bc_prob, k=1)[0]

            # Technical Layer

            st_prob = [0.30, 0.20, 0.40, 0.10]
            ht_prob = [0.30, 0.20, 0.40, 0.10]
            ue_prob = [0.60, 0.40]

            st_choice = random.choices(software_technology_domain, weights=st_prob, k=1)[0]
            ht_choice = random.choices(hardware_technology_domain, weights=ht_prob, k=1)[0]
            ue_choice = random.choices(user_experience_domain, weights=ue_prob, k=1)[0]

            # Risk Layer

            es_prob = [0.20, 0.20, 0.10, 0.50]
            ra_prob = [0.20, 0.20, 0.10, 0.50]
            br_prob = [0.20, 0.20, 0.10, 0.50]

            es_choice = random.choices(executive_support_domain, weights=es_prob, k=1)[0]
            ra_choice = random.choices(resource_availability_domain, weights=ra_prob, k=1)[0]
            br_choice = random.choices(business_requirements_domain, weights=br_prob, k=1)[0]

            # Cost Layer

            hw_prob = [0.30, 0.45, 0.25]
            sw_prob = [0.25, 0.50, 0.25]
            fa_prob = [0.50, 0.25, 0.15, 0.10]

            hw_choice = random.choices(hardware_maintenance_domain, weights=hw_prob, k=1)[0]
            sw_choice = random.choices(software_maintenance_domain, weights=sw_prob, k=1)[0]
            fa_choice = random.choices(funding_availability_domain, weights=fa_prob, k=1)[0]

            # Modernization Layer

            ma_prob = [0.10, 0.30, 0.40, 0.20]
            cr_prob = [0.30, 0.70]

            ma_choice = random.choices(modern_architecture_domain, weights=ma_prob, k=1)[0]
            cr_choice = random.choices(cloud_readiness_domain, weights=cr_prob, k=1)[0]

            number_users = random.randint(1, 3000)
            application_age = random.randint(1, 15)


            data_dict = ({ "APPLICATION" : app_name, 
                           "CLIENT_SATISFACTION" : cs_choice,
                           "BUSINESS_CRITICALITY" : bc_choice,
                           "NUMBER_USERS" : str(number_users),
                           "SOFTWARE_TECHNOLOGY" : st_choice,
                           "HARDWARE_TECHNOLOGY" : ht_choice,
                           "USER_EXPERIENCE" : ue_choice,
                           "EXECUTIVE_SUPPORT" : es_choice,
                           "RESOURCE_AVAILABILITY" : ra_choice,
                           "BUSINESS_REQUIREMENTS" : br_choice,
                           "HARDWARE_MAINTENANCE" : hw_choice,
                           "SOFTWARE_MAINTENANCE" : sw_choice,
                           "FUNDING_AVAILABILITY" : fa_choice,
                           "APPLICATION_AGE" : str(application_age),
                           "MODERN_ARCHITECTURE" : ma_choice,
                           "CLOUD_READINESS" : cr_choice })
            data_list.append(data_dict)

        return data_list


    def display_output(self):

        pass







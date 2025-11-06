# KnowledgeBaseC

class KnowledgeBaseC:
    
    def __init__(self):
        self.data_dictionary = {}
        self.rules = []  # [] of {}

        self.__load_data_dictionary()
        self.__load_rules()



    def get_data_dictionary(self) -> {}:

        return self.data_dictionary


    def set_data_dictionary(self, data_dictionary):

        self.data_dictionary = data_dictionary


    def get_rules(self) -> []:
        return self.rules

    def set_rules(self, rules):
        self.rules = rules


    # Private methods.

    def __load_data_dictionary(self):

        self.data_dictionary = { "LAYER" : "business_value" }

        application = "App1"
        current_effectiveness = "good"

        self.data_dictionary.update({ "application" : application, "current_effectiveness" : current_effectiveness })


    def __load_rules(self):

      #  condition = "[(cam is 55) AND (home is Westboro)] OR [(cam is 60) AND (city is Ottawa)] ;"

        # Rule 1.

        condition = "[(layer is business_value)] ;"
        action = "SET business_value to High"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 2.

        condition = "[(layer is business_value)] AND [(current_effectiveness is good) OR (current_effectiveness is great)] ;"
        action = "SET business_value to High"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3.

        condition = "[(layer is business_value)] AND [(current_effectiveness is okay) OR (current_effectiveness is bad)] ;"
        action = "SET business_value to Low"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 4.

        condition = "[(business_value is High)] OR [(business_value is Low)] ;"
        action = "SET business_value_rules to Complete"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 5.

        condition = "[(business_value_rules is Complete)] ;"
        action = "ADD_NODE $application$ to $business_value$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 6.

        condition = "[(business_value_rules is Complete)] ;"
        action = "SET layer to technical condition"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)





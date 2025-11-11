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

        self.data_dictionary = { "LAYER" : "business_value", "CURRENT_NODE" : "Start" }

     #   application = "App1"
     #   current_effectiveness = "good"
     #   operating_system = "good"

     #   self.data_dictionary.update({ "APPLICATION" : application, "CURRENT_EFFECTIVENESS" : current_effectiveness,
      #                                "OPERATING_SYSTEM" : "okay",
      #                                "CURRENT_NODE" : "Start"})


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

        # Rule 3a.

        condition = "[(business_value is Low)] ;"
        action = "SET edge_weight to 1"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3a1.

        condition = "[(business_value is Low)] ;"
        action = "SET node_id to 1"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3b.

        condition = "[(business_value is High)] ;"
        action = "SET edge_weight to 3"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3b1.

        condition = "[(business_value is High)] ;"
        action = "SET node_id to 2"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 4.

        condition = "[(business_value is High)] OR [(business_value is Low)] ;"
        action = "SET business_value_rules to Complete"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 5.

        condition = "[(business_value_rules is Complete)] ;"
      #  action = "ADD_NODE $application$ to BV-$business_value$"
        action = "ADD_NODE $application$ to $node_id$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 6.

        condition = "[(business_value_rules is Complete)] ;"
    #    action = "ADD_EDGE BV-$business_value$ to $current_node$ weighted $edge_weight$"
        action = "ADD_EDGE $node_id$ to $current_node$ weighted $edge_weight$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 7.

        condition = "[(business_value_rules is Complete)] ;"
  #      action = "SET current_node to BV-$business_value$"
        action = "SET current_node to $node_id$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 8.

        condition = "[(business_value_rules is Complete)] ;"
        action = "SET layer to technical_condition"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)


        # Technical Condition

        # Rule 1.

        condition = "[(layer is technical_condition)] ;"
        action = "SET technical_condition to High"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 2.

        condition = "[(layer is technical_condition)] AND [(operating_system is good) OR (operating_system is great)] ;"
        action = "SET technical_condition to High"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3.

        condition = "[(layer is technical_condition)] AND [(operating_system is okay) OR (operating_system is bad)] ;"
        action = "SET technical_condition to Low"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3a.

        condition = "[(technical_condition is Low)] ;"
        action = "SET edge_weight to 1"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3a1.

        condition = "[(technical_condition is Low)] ;"
        action = "SET node_id to $node_id$.1"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3b.

        condition = "[(technical_condition is High)] ;"
        action = "SET edge_weight to 3"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3b1.

        condition = "[(technical_condition is High)] ;"
        action = "SET node_id to $node_id$.2"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)


        # Rule 4.

        condition = "[(technical_condition is High)] OR [(technical_condition is Low)] ;"
        action = "SET technical_condition_rules to Complete"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 5.

        condition = "[(technical_condition_rules is Complete)] ;"
    #    action = "ADD_NODE $application$ to TC-$technical_condition$"
        action = "ADD_NODE $application$ to $node_id$"
        
        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 6.

        condition = "[(technical_condition_rules is Complete)] ;"
  #      action = "ADD_EDGE TC-$technical_condition$ to $current_node$ weighted $edge_weight$"
        action = "ADD_EDGE $node_id$ to $current_node$ weighted $edge_weight$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 7.

        condition = "[(technical_condition_rules is Complete)] ;"
  #      action = "SET current_node to TC-$technical_condition$"
        action = "SET current_node to $node_id$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 8.

        condition = "[(technical_condition_rules is Complete)] ;"
        action = "SET layer to application_risk"
  #      action = "SET layer to business_value"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 9.

        #condition = "[(technical_condition_rules is Complete)] ;"
        #action = "SET current_node to Start"

       # rule = { "condition" : condition, "action" : action }
       # self.rules.append(rule)



        # Risk

        # Rule 1 - #default

        condition = "[(layer is application_risk)] ;"
        action = "SET application_risk to High"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 2.

        condition = "[(layer is application_risk)] AND [(risk is good) OR (risk is great)] ;"
        action = "SET application_risk to Low"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3.

        condition = "[(layer is application_risk)] AND [(risk is okay) OR (risk is bad)] ;"
        action = "SET application_risk to High"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3a.

        condition = "[(application_risk is Low)] ;"
        action = "SET edge_weight to 1"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3a1.

        condition = "[(application_risk is Low)] ;"
        action = "SET node_id to $node_id$.1"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3b.

        condition = "[(application_risk is High)] ;"
        action = "SET edge_weight to 3"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3b1.

        condition = "[(application_risk is High)] ;"
        action = "SET node_id to $node_id$.2"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 4.

        condition = "[(application_risk is High)] OR [(application_risk is Low)] ;"
        action = "SET application_risk_rules to Complete"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 5.

        condition = "[(application_risk_rules is Complete)] ;"
     #   action = "ADD_NODE $application$ to RI-$application_risk$"
        action = "ADD_NODE $application$ to $node_id$"
        
        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 6.

        condition = "[(application_risk_rules is Complete)] ;"
   #     action = "ADD_EDGE RI-$application_risk$ to $current_node$ weighted $edge_weight$"
        action = "ADD_EDGE $node_id$ to $current_node$ weighted $edge_weight$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 7.

        condition = "[(application_risk_rules is Complete)] ;"
 #       action = "SET current_node to RI-$application_risk$"
        action = "SET current_node to $node_id$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 8.

        condition = "[(application_risk_rules is Complete)] ;"
        action = "SET layer to application_cost"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 9.

      #  condition = "[(application_risk_rules is Complete)] ;"
     #   action = "SET current_node to Start"

     #   rule = { "condition" : condition, "action" : action }
      #  self.rules.append(rule)




        # Cost

        # Rule 1 - default

        condition = "[(layer is application_cost)] ;"
        action = "SET application_cost to High"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 2.

        condition = "[(layer is application_cost)] AND [(cost is good) OR (cost is great)] ;"
        action = "SET application_cost to Low"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3.

        condition = "[(layer is application_cost)] AND [(cost is okay) OR (cost is bad)] ;"
        action = "SET application_cost to High"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3a.

        condition = "[(application_cost is Low)] ;"
        action = "SET edge_weight to 1"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3a1.

        condition = "[(application_cost is Low)] ;"
        action = "SET node_id to $node_id$.1"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3b.

        condition = "[(application_cost is High)] ;"
        action = "SET edge_weight to 3"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 3a1.

        condition = "[(application_cost is High)] ;"
        action = "SET node_id to $node_id$.2"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 4.

        condition = "[(application_cost is High)] OR [(application_cost is Low)] ;"
        action = "SET application_cost_rules to Complete"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 5.

        condition = "[(application_cost_rules is Complete)] ;"
  #      action = "ADD_NODE $application$ to CO-$application_cost$"
        action = "ADD_NODE $application$ to $node_id$"
        
        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 6.

        condition = "[(application_cost_rules is Complete)] ;"
   #     action = "ADD_EDGE CO-$application_cost$ to $current_node$ weighted $edge_weight$"
        action = "ADD_EDGE $node_id$ to $current_node$ weighted $edge_weight$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 7.

        condition = "[(application_cost_rules is Complete)] ;"
    #    action = "SET current_node to CO-$application_cost$"
        action = "SET current_node to $node_id$"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 8.

        condition = "[(application_cost_rules is Complete)] ;"
        action = "SET layer to business_value"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)

        # Rule 9.

        condition = "[(application_cost_rules is Complete)] ;"
        action = "SET current_node to Start"

        rule = { "condition" : condition, "action" : action }
        self.rules.append(rule)
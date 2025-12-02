# KnowledgeBaseC

# Import classes.

import json

# Import Project classes.

from PlannerKnowledgeGraphC import PlannerKnowledgeGraphC

import Global


class KnowledgeBaseC:
    
    # Constructor

    def __init__(self, environment):

        try:

            # Set the Knowledge Base attributes.

            self.environment = environment

            self.data_dictionary = {}
            self.rules = []  # [] of {}
            self.knowledge_graph = None

            self.__load_data_dictionary()

            # Load the rules from the JSON rules file.

            self.__load_rules_from_json()

        except Exception as e:

            # Catch, log and raise all exceptions.

            print("KnowledgeBaseC Exception:", e)
            raise e


    # get_data_dictionary

    def get_data_dictionary(self) -> {}:

        return self.data_dictionary


    # set_data_dictionary

    def set_data_dictionary(self, data_dictionary):

        self.data_dictionary = data_dictionary


    # get_rules

    def get_rules(self) -> []:
        return self.rules


    # set_rules

    def set_rules(self, rules):
        self.rules = rules


    # get_knowledge_graph

    def get_knowledge_graph(self):

        return self.knowledge_graph


    # set_knowledge_graph

    def set_knowledge_graph(self, knowledge_graph):

        self.knowledge_graph = knowledge_graph


    # Private methods.

    # __load_data_dictionary

    def __load_data_dictionary(self):
        
        # Load the initial data set.  Currently, it is to initialize the layer and the
        # current node.

        self.data_dictionary = { "LAYER" : "business_value", "CURRENT_NODE" : "Start" }


    # __load_rules_from_json

    def __load_rules_from_json(self):

        try:

            # Open the JSON file specified in the Environment in read mode.

            with open(self.environment.get_rules_file(), 'r') as f:

                # Load the JSON data into a Python dictionary
                rules = json.load(f)
        
            for rule in rules:

                if Global._debug: print ("Loading rule -->", rule)

                rule = { "ID" : rule["id"],
                         "name" : rule["name"], 
                         "description" : rule["description"],
                         "condition" : rule["condition"], 
                         "action" : rule["action"]
                        }

                self.rules.append(rule)

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("KnowledgeBaseC Exception:", e)
            raise e



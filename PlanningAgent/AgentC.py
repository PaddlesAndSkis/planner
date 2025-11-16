# AgentC

# Import libraries.

import re

# Import Project classes.

import Global

from PlannerBooleanExpressionEvaluatorC import PlannerBooleanExpressionEvaluatorC
from PlannerActionEvaluatorConstructC import PlannerActionEvaluatorConstructC
from PlannerKnowledgeGraphC import PlannerKnowledgeGraphC

from EnvironmentC import EnvironmentC
from KnowledgeBaseC import KnowledgeBaseC
from PerceptionC import PerceptionC
from RulesEngineC import RulesEngineC


class AgentC:

    # Constructor

    def __init__(self):
        
        # Create the Agent modules.

        self.perception = PerceptionC()
        self.knowledge_base = KnowledgeBaseC()
        self.rules_engine = RulesEngineC()



    # add_to_data_dictionary

    def add_to_data_dictionary(self, data_dictionary):

        # Set the data dictionary in the Agent's Knowledge Base.

        self.knowledge_base.set_data_dictionary(data_dictionary)


    def start_planning_session(self, environment):

        self.environment = environment

        # Loop of prompts:
        # 1. Query for shortest path
        # 2. Query for longest path

        print ("Hello")

        kb = KnowledgeBaseC()
        planner_knowledge_graph = PlannerKnowledgeGraphC()

        plannerActionEvaluator = PlannerActionEvaluatorConstructC()

        # Get the data set from the Environment.

        data_list = self.environment.load_data()

        print ("dat_list = ", data_list)
        # Get the rules.

        rules = kb.get_rules()

        # Get the initial data dictionary.

        data_dictionary = kb.get_data_dictionary()

        for datum in data_list:

            data_dictionary.update(datum)

            # MOVE THE FOLLOWING TO THE RULESENGINEC class.

            # e.g.:
            # self.rules_engine.set_kb(kb)
            # planner_knowledge_graph = self.rules_engine.create_graph()
            # self.perception.set_knowledge_graph(planner_knowledge_graph)
            # self.perception.take_inputs()

            for rule in rules:

                if Global._debug: print ("Evaluating:", rule)
                if Global._debug: print ("data_dictionary is:", data_dictionary)

                condition = rule["condition"]

                # Resolve any variables that are present in the condition.

                condition = self.resolveVariables(condition, data_dictionary)

                plannerBooleanExpressionEvaluator = PlannerBooleanExpressionEvaluatorC(condition, data_dictionary)
                conditionBooleanResult = plannerBooleanExpressionEvaluator.evaluateBooleanExpression()

                print ("The final result is: ", conditionBooleanResult)

            
                if (conditionBooleanResult):

                    # Get the operation / action that this plant will do during its growth spurt.

                    action = rule["action"]

                    # Resolve any variables that are present in the action.

                    action = self.resolveVariables(action, data_dictionary)
                    if Global._debug: print ("Firing...", action)

                    # Invoke the action for the plant.

             #       plannerActionEvaluator = PlannerActionEvaluatorConstructC()
                    data_dictionary = plannerActionEvaluator.invokeAction(action, data_dictionary, planner_knowledge_graph)

                    if Global._debug: print ("*********************data_dictionary is now:", data_dictionary)



        # Move THE FOLLOWING to the PerceptionC class (need to pass in the planner_knowledge_graph) so that queries
        # can be made on the data.


        # e.g.:
        # self.perception.set_knowledge_graph(planner_knowledge_graph)

        planner_knowledge_graph.print_node_applications("1.1.1.1", "application")
        planner_knowledge_graph.print_leaf_nodes("application")
        planner_knowledge_graph.add_end_node()
        
        planner_knowledge_graph.print()
        planner_knowledge_graph.print_shortest_path()
        planner_knowledge_graph.print_longest_path()

        print("If you know the name of the node, you can iterate through all the nodes and get the name:")
        planner_knowledge_graph.search_graph_by_name("Low_business_value")
        planner_knowledge_graph.search_graph_by_name("Low_technical_condition")

        print("If you want to know which nodes have Low_business_value, Low_technical_condition, you must BFS:")
        planner_knowledge_graph.search_graph_by_names('Low_business_value', 'Low_technical_condition')

        print("If you want to get all the edges in a breadth first search:")
        planner_knowledge_graph.breadth_first_search('Start')

        print("If you want to know which nodes have low business value, high technical condition, you must BFS:")
        planner_knowledge_graph.search_graph_by_names('Low_business_value', 'Low_technical_condition')
        
        print("If you want to know which nodes have high application risk, low modernization, you must BFS:")
        planner_knowledge_graph.search_graph_by_names('High_application_risk', 'Low_modernization')

        planner_knowledge_graph.print_node_applications("1", "application")
        planner_knowledge_graph.print_node_applications("2", "application")


    # resolveVariables

    def resolveVariables(self, stringLine, dataDictionary):     

        # Split the string line into its tokens based on the regex expression.

        tempStringArray = re.split(r'(\$.*?\$)', stringLine)

        print ("stringLine = ", stringLine)
        print ("tempStringArray = ", tempStringArray)

        newStringLine = ""

        # Iterate over the tokens.

        for token in tempStringArray:

            # Check to see if the token is a variable (e.g., $var$).

            if (re.search(r"(\$.*?\$)", token)):

                # Variable is present - remove the $ delimiters.

                token = token[1:len(token)-1]

                # Look up the data value for this variable in the 
                # data dictionary Hashtable and set that as the new token
                # value.

                token = dataDictionary[token.upper()]

                if Global._debug: print ("TOKEN   NOW IS", token)

            # Set the new string (e.g., condition, action) to include the
            # token value.

            newStringLine = newStringLine + token 

        if Global._debug: print ("Resolved variables:", newStringLine)

        # Return the new string that will include all resolved variables.

        return newStringLine

    

    




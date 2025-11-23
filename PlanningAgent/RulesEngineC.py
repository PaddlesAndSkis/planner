# RulesEngineC

# Import classes.

import re

# Import Project classes.

from PlannerBooleanExpressionEvaluatorC import PlannerBooleanExpressionEvaluatorC
from PlannerActionEvaluatorConstructC import PlannerActionEvaluatorConstructC
from PlannerKnowledgeGraphC import PlannerKnowledgeGraphC

import Global

class RulesEngineC():

    # Default Constructor.

    def __init__(self, kb):

        try:

            self.kb = kb
            self.rules = kb.get_rules()

            # Get the initial data dictionary.

            self.planner_knowledge_graph = PlannerKnowledgeGraphC()

            self.plannerActionEvaluator = PlannerActionEvaluatorConstructC()

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("RulesEngineC Exception:", e)
            raise e


    # Only provide a getter for the knowledge graph - only Rules Engine can update it.

    # get_knowledge_graph

    def get_knowledge_graph(self) -> PlannerKnowledgeGraphC:

        return self.planner_knowledge_graph


    # invoke_rules

    def invoke_rules(self, data_dictionary) -> {}:

        try:

            for rule in self.rules:

                if Global._debug: print ("Evaluating Rule:", rule)
                if Global._debug: print ("Data Dictionary:", data_dictionary)

                condition = rule["condition"]

                # Resolve any variables that are present in the condition.

                condition = self.resolveVariables(condition, data_dictionary)

                plannerBooleanExpressionEvaluator = PlannerBooleanExpressionEvaluatorC(condition, data_dictionary)
                conditionBooleanResult = plannerBooleanExpressionEvaluator.evaluateBooleanExpression()

                if Global._debug: print ("Condition Result:", conditionBooleanResult)

                # Check to see if the condition is True.

                if (conditionBooleanResult):

                    # Get the action to invoke.

                    action = rule["action"]

                    # Resolve any variables that are present in the action.

                    action = self.resolveVariables(action, data_dictionary)
                    if Global._debug: print ("Firing...", action)

                    if Global._info: print ("A rule named", rule["name"], "has been activated.")
                    if Global._info: print (rule["description"])

                    # Update the action with the resolved variables.
                    
               #     rule["action"] = action

                    # Invoke the action and update the data dictionary.

              #      data_dictionary = self.plannerActionEvaluator.invokeAction(rule, data_dictionary, self.planner_knowledge_graph)
                    data_dictionary = self.plannerActionEvaluator.invokeAction(action, data_dictionary, self.planner_knowledge_graph)

                    if Global._debug: print ("Data Dictionary Post-Action:", data_dictionary)

            # Return the new data dictionary.

            return data_dictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("RulesEngineC Exception:", e)
            raise e


    # resolveVariables

    def resolveVariables(self, stringLine, dataDictionary) -> str:     

        try:

            # Split the string line into its tokens based on the regex expression.

            tempStringArray = re.split(r'(\$.*?\$)', stringLine)

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

                    if Global._debug: print ("Current token:", token)

                # Set the new string (e.g., condition, action) to include the
                # token value.

                newStringLine = newStringLine + token 

            if Global._debug: print ("Resolved variables:", newStringLine)

            # Return the new string that will include all resolved variables.

            return newStringLine

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("RulesEngineC Exception:", e)
            raise e

    
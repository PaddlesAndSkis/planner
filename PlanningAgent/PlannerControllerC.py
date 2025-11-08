# PlannerControllerC

import re

# Import Project classes.

import Global

from PlannerBooleanExpressionEvaluatorC import PlannerBooleanExpressionEvaluatorC
from PlannerActionEvaluatorConstructC import PlannerActionEvaluatorConstructC
from KnowledgeBaseC import KnowledgeBaseC



class PlannerControllerC:


    def __init__(self, agent, environment):

        self.agent = agent
        self.environment = environment


    def start_planning_session(self):

        # Loop of prompts:
        # 1. Query for shortest path
        # 2. Query for longest path

        print ("Hello")

        kb = KnowledgeBaseC()

        rules = kb.get_rules()
        data_dictionary = kb.get_data_dictionary()

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

                plannerActionEvaluator = PlannerActionEvaluatorConstructC()
                data_dictionary = plannerActionEvaluator.invokeAction(action, data_dictionary)

                if Global._debug: print ("*********************data_dictionary is now:", data_dictionary)


    def resolveVariables(self, stringLine, dataDictionary):     

        # into its tokens.

        tempStringArray = re.split(r"/(\w*\$\w+\$)/", stringLine)
        #self.tempExpression = re.split(r"([\!\[\]\(\)])", booleanExpression)

        newStringLine = ""

        # Iterate over the tokens.

        for token in tempStringArray:

            # Check to see if the token is a variable (e.g., $var$).

            #if (token.match(/\w*\$\w+\$/))

            if (re.search(r"/(\w*\$\w+\$)/", token, flags=0)):

               # Variable is present - remove the $ delimiters.

               token = token.delete("$")

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

    
        

    #    condition = "[(cam is 55) AND (home is Westboro)] OR [(cam is 60) AND (city is Ottawa)] ;"
        
        
        # Add the data dictionary to the Agent.

     #   dataDictionary = {"CAM" : "55", "HOME" : "Westboro", "CITY" : "Ottawa"}

    #    self.agent.add_to_data_dictionary(dataDictionary)

    #    plannerBooleanExpressionEvaluator = PlannerBooleanExpressionEvaluatorC(condition, dataDictionary)
   #     conditionBooleanResult = plannerBooleanExpressionEvaluator.evaluateBooleanExpression()


    #    print ("The final result is: ", conditionBooleanResult)






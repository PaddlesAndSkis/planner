# PlannerControllerC

# Import Project classes.

from PlannerBooleanExpressionEvaluatorC import PlannerBooleanExpressionEvaluatorC
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

            condition = rule["condition"]

            plannerBooleanExpressionEvaluator = PlannerBooleanExpressionEvaluatorC(condition, data_dictionary)
            conditionBooleanResult = plannerBooleanExpressionEvaluator.evaluateBooleanExpression()

            print ("The final result is: ", conditionBooleanResult)


        

    #    condition = "[(cam is 55) AND (home is Westboro)] OR [(cam is 60) AND (city is Ottawa)] ;"
        
        
        # Add the data dictionary to the Agent.

     #   dataDictionary = {"CAM" : "55", "HOME" : "Westboro", "CITY" : "Ottawa"}

    #    self.agent.add_to_data_dictionary(dataDictionary)

    #    plannerBooleanExpressionEvaluator = PlannerBooleanExpressionEvaluatorC(condition, dataDictionary)
   #     conditionBooleanResult = plannerBooleanExpressionEvaluator.evaluateBooleanExpression()


    #    print ("The final result is: ", conditionBooleanResult)






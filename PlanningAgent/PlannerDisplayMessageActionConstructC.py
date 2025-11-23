# PlannerDisplayMessageActionConstructC

# Import Project classes.

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA

# Import libraries.

import Global


class PlannerDisplayMessageActionConstructC(PlannerGraphActionConstructA):
   
    # Constructor

    def __init__(self):
        super().__init__()

    # invokeAction

    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph) -> {}:

        try:

            if Global._debug: print ("Display_Message Action actionData:", actionData)
            if Global._debug: print ("Display_Message Action dataDictionary:", dataDictionary)

            # "Display_Message <message>"

            message  = " ".join(actionData[1:])

            # Add the graph node to the Planner Knowledge Graph.

            print ("\n", message, "\n")

            return dataDictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerAddNodeActionConstructC Exception:", e)
            raise e

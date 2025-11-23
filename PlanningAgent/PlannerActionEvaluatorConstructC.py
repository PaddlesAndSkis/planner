# PlannerActionEvaluatorConstructC
#
# Class that evaluates the rule actions.

# Import libraries.

from PlannerAddActionConstructC import PlannerAddActionConstructC
from PlannerAddNodeActionConstructC import PlannerAddNodeActionConstructC
from PlannerAddEdgeActionConstructC import PlannerAddEdgeActionConstructC
from PlannerSetActionConstructC import PlannerSetActionConstructC
from PlannerSubtractActionConstructC import PlannerSubtractActionConstructC
from PlannerDisplayNodeActionConstructC import PlannerDisplayNodeActionConstructC
from PlannerDisplayMessageActionConstructC import PlannerDisplayMessageActionConstructC

import Global


# Class PlanterboxActionEvaluatorConstructC

class PlannerActionEvaluatorConstructC:

    # Constructor

    def __init__(self):

        # Create a Hashtable of the set of allowable condition constructs.

        self.actionConstructLibrary = {}
        self.actionConstructLibrary["ADD"]             = PlannerAddActionConstructC()
        self.actionConstructLibrary["ADD_NODE"]        = PlannerAddNodeActionConstructC()
        self.actionConstructLibrary["ADD_EDGE"]        = PlannerAddEdgeActionConstructC()
        self.actionConstructLibrary["SET"]             = PlannerSetActionConstructC()
        self.actionConstructLibrary["SUBTRACT"]        = PlannerSubtractActionConstructC()
        self.actionConstructLibrary["DISPLAY_NODE"]    = PlannerDisplayNodeActionConstructC()
        self.actionConstructLibrary["DISPLAY_MESSAGE"]    = PlannerDisplayMessageActionConstructC()
        

    # invokeAction
    #
    # [in]: rule - the rule action to take once the condition constructs evaluate to True
    # [in]: dataDictionary - the dictionary of variables (keyword-value pairs)

    def invokeAction(self, action, dataDictionary, plannerKnowledgeGraph) -> {}:

        try:

            if Global._debug: print ("Invoking the rule action:", action)

            # Split the action constructs by the space character.

            constructComponents = action.split(" ")

            # Remove the action's brackets.  The actionData consists of all the 
            # other components of the action that will be left up to the individual
            # action to interpret.

            actionComponent = constructComponents[0].upper() #.delete('()').strip
            actionData      = constructComponents

            if Global._debug: print("actionComponent =", actionComponent)

            # Invoke the action.

            dataDictionary = self.actionConstructLibrary[actionComponent].invokeAction(dataDictionary, actionData, plannerKnowledgeGraph)

            return dataDictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerActionEvaluatorConstructC Exception:", e)
            raise e

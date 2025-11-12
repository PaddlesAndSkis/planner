# PlannerActionEvaluatorConstructC
#
# Class that evaluates the rule actions.

# Import libraries.

from PlannerSetActionConstructC import PlannerSetActionConstructC
from PlannerAddActionConstructC import PlannerAddActionConstructC
from PlannerAddNodeActionConstructC import PlannerAddNodeActionConstructC
from PlannerAddEdgeActionConstructC import PlannerAddEdgeActionConstructC

import Global


# Class PlanterboxActionEvaluatorConstructC

class PlannerActionEvaluatorConstructC:

    # Constructor

    def __init__(self):

        # Create a Hashtable of the set of allowable condition constructs.

        self.actionConstructLibrary = {}
        self.actionConstructLibrary["SET"]             = PlannerSetActionConstructC()
        self.actionConstructLibrary["ADD"]             = PlannerAddActionConstructC()
        self.actionConstructLibrary["ADD_NODE"]        = PlannerAddNodeActionConstructC()
        self.actionConstructLibrary["ADD_EDGE"]        = PlannerAddEdgeActionConstructC()
        


    # invokeAction
    #
    # [in]: action - the action to take once the condition constructs evaluate to True
    # [in]: dataDictionary - the dictionary of variables (keyword-value pairs)

    def invokeAction(self, action, dataDictionary, plannerKnowledgeGraph):

        if Global._debug: print ("INVOKING ACTION!!!")

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

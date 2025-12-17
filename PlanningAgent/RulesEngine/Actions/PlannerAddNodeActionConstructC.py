# PlannerAddNodeActionConstructC

# Import Project classes.

from RulesEngine.Actions.PlannerActionConstructA import PlannerActionConstructA
from RulesEngine.Actions.PlannerGraphActionConstructA import PlannerGraphActionConstructA

# Import libraries.

import Global


class PlannerAddNodeActionConstructC(PlannerGraphActionConstructA):
   
    # Constructor

    def __init__(self):
        super().__init__()


    # invokeAction

    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph) -> {}:

        try:

            if Global._debug: print ("Add_Npde Action actionData:", actionData)
            if Global._debug: print ("Add_Node Action dataDictionary:", dataDictionary)

            # "ADD_NODE <attribute_name> <attribute_value> to <node_id> named <node_name>"

            attribute_name  = actionData[1] 
            attribute_value = actionData[2] 
            node_id         = actionData[4]  
            node_name       = actionData[6]  

            if Global._debug: print ("Add_Node Action: a node with", attribute_name, " ", attribute_value, "will be added to", node_id, "named", node_name)

            # Add the graph node to the Planner Knowledge Graph.

            plannerKnowledgeGraph.add_node(node_id, node_name, attribute_name, attribute_value)

            return dataDictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerAddNodeActionConstructC Exception:", e)
            raise e

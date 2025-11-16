# PlannerAddNodeActionConstructC

# Import Project classes.

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA

# Import libraries.

import Global


class PlannerAddNodeActionConstructC(PlannerGraphActionConstructA):
   
    def __init__(self):
        super().__init__()


    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph):

        print ("In ADD_NODE with", actionData)
        print ("In ADD_NODE with", dataDictionary)

        # "ADD_NODE <attribute_name> <attribute_value> to <node_id> named <node_name>"

        attribute_name  = actionData[1] #.upper()  # .strip()
        attribute_value = actionData[2] #.upper()  # .strip()
        node_id         = actionData[4]  #.delete('()').strip
        node_name       = actionData[6]  #.delete('()').strip

        print ("In ADD_NODE with", attribute_name, " ", attribute_value, "will be added to", node_id, "named", node_name)

        # Add the graph node to the Planner Knowledge Graph.

        plannerKnowledgeGraph.add_node(node_id, node_name, attribute_name, attribute_value)

        return dataDictionary


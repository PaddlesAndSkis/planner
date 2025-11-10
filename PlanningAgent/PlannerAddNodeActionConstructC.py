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

        # "ADD_NODE <application> to <node_name>"

        application = actionData[1] #.upper()  # .strip()
        node_name   = actionData[3]  #.delete('()').strip

        print ("In ADD_NODE with application to add to node_name: ", application, "will be added to", node_name)

        # Add the graph node to the Planner Knowledge Graph.

        plannerKnowledgeGraph.add_node(node_name, application)

        # self.G.add_node(myValue, node=myValue, application=myKey)

        return dataDictionary


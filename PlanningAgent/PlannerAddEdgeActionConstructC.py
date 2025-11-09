# PlannerAddNodeActionConstructC

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA
import Global

import networkx as nx


class PlannerAddEdgeActionConstructC(PlannerGraphActionConstructA):
   
    def __init__(self):
        super().__init__()

    def invokeAction(self, dataDictionary, actionData):

        print ("In ADD_EDGE with", actionData)
        print ("In ADD_EDGE with", dataDictionary)

        # Add dest to current

        dest_node     = actionData[1].upper()  # .strip()
        current_node  = actionData[3]  #.delete('()').strip

        print ("In ADD_EDGE with current_node : dest_node", current_node, " ->", dest_node)

        self.G.add_edge(current_node, dest_node, weight=1)

        print("!!!!!!!!!8888888888888888888888888888888888888888888888888888888888888!!!!!! EDGES:", self.G.edges)

        return dataDictionary


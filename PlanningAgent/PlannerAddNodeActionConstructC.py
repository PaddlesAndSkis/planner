# PlannerAddNodeActionConstructC

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA
import Global

import networkx as nx


class PlannerAddNodeActionConstructC(PlannerGraphActionConstructA):
   
    def __init__(self):
        super().__init__()


    def invokeAction(self, dataDictionary, actionData):

        print ("In ADD_NODE with", actionData)
        print ("In ADD_NODE with", dataDictionary)

        myKey   = actionData[1].upper()  # .strip()
        myValue = actionData[3]  #.delete('()').strip

        print ("In ADD_NODE with myKey : myValue", myKey, " ->", myValue)

        self.G.add_node(myValue, node=myValue, application=myKey)

        print("!!!!!!!!!!!!!!! NODES:", self.G.nodes)

        return dataDictionary


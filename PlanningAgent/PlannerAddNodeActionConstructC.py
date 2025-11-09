# PlannerAddNodeActionConstructC

from PlannerActionConstructA import PlannerActionConstructA
import Global

import networkx as nx


class PlannerAddNodeActionConstructC(PlannerActionConstructA):
   
    def __init__(self):
        self.G = nx.DiGraph()


    def invokeAction(self, dataDictionary, actionData):

        print ("In ADD_NODE with", actionData)
        print ("In ADD_NODE with", dataDictionary)

        myKey   = actionData[1].upper()  # .strip()
        myValue = actionData[3]  #.delete('()').strip

        print ("In ADD_NODE with myKey : myValue", myKey, " ->", myValue)

        self.G.add_node(myValue, node=myValue, application=myKey)

        dataDictionary[myKey] = myValue

        return dataDictionary


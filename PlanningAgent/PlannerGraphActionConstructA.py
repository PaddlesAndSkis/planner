# PlannerAddNodeActionConstructC

from PlannerActionConstructA import PlannerActionConstructA
import Global

import networkx as nx
from abc import ABC, abstractmethod

class PlannerGraphActionConstructA(PlannerActionConstructA, ABC):
   
    def __init__(self):
        self.G = nx.DiGraph()
        self.G.add_node("Start", node="Start", application="n/a")


    def invokeAction(self, dataDictionary, actionData):

        print ("ABATRACT CLSSS")

        return None


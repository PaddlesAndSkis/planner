# PlannerAddNodeActionConstructC

# Import Project classes.

from PlannerActionConstructA import PlannerActionConstructA
import Global

# Import libraries.

from abc import ABC, abstractmethod


class PlannerGraphActionConstructA(PlannerActionConstructA, ABC):
   
    def __init__(self):
        pass


    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph):

        print ("ABATRACT CLSSS")

        return None


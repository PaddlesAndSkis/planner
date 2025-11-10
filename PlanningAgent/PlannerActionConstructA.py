# PlannerActionConstructA

# Import libraries.

from abc import ABC, abstractmethod

class PlannerActionConstructA(ABC):

    # Constructor

    def __init__(self):
        pass


    def invokeAction(self, dataDictionary, actionHash, plannerKnowledgeGraph):
       
        print ("PlannerboxActionConstructA is abstract.")



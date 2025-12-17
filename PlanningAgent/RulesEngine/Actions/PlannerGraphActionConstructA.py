# PlannerGraphActionConstructA

# Import Project classes.

from RulesEngine.Actions.PlannerActionConstructA import PlannerActionConstructA
import Global

# Import libraries.

from abc import ABC, abstractmethod


class PlannerGraphActionConstructA(PlannerActionConstructA, ABC):
   
    # Constructor

    def __init__(self):
        pass


    # invokeAction

    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph) -> {}:

        print ("ABSTRACT CLSSS")

        return None


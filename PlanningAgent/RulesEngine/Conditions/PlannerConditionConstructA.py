# PlannerConditionConstructA

# Import libraries.

from abc import ABC, abstractmethod


class PlannerConditionConstructA(ABC):

    # Constructor

    def __init__(self):
        pass


    # evaluate

    def evaluate(self, dataDictionary, conditionHash) -> bool:
        
        # Raise an exception if the abstract class is called.

        raise Exception("PlannerConditionConstructA is abstract.")







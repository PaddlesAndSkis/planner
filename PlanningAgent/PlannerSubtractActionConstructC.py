# PlannerSubtractActionConstructC

# Import Project classes.

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA

import Global


class PlannerSubtractActionConstructC(PlannerGraphActionConstructA):

    # Constructor
       
    def __init__(self):
        super().__init__()


    # invokeAction

    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph) -> {}:

        try:

            # "SUBTRACT <value> from <dictionary_variable>"

            if Global._debug: print ("Subtract Action actionData:", actionData)
            if Global._debug: print ("Subtract Action dataDictionary:", dataDictionary)

            # Extract the value and the data dictionary variable.

            value               = actionData[1] #.upper()  # .strip()
            dictionary_variable = actionData[3].upper()  #.delete('()').strip

            # Subtract the value from the dictionary variable.

            if Global._debug: print ("Subtract Action:", value, "will be subtracted from", dictionary_variable)

            dictionary_variable_value = int(dataDictionary[dictionary_variable]) - int(value)

            # Uupdate the data dictionary with the new value..

            dataDictionary.update({dictionary_variable : str(dictionary_variable_value)})

            return dataDictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerSubtractActionConstructC Exception:", e)
            raise e





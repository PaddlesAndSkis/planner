# PlannerAddActionConstructC

# Import Project classes.

from RulesEngine.Actions.PlannerActionConstructA import PlannerActionConstructA
from RulesEngine.Actions.PlannerGraphActionConstructA import PlannerGraphActionConstructA

# Import libraries.

import Global


class PlannerAddActionConstructC(PlannerGraphActionConstructA):
   
    # Constructor

    def __init__(self):
        super().__init__()

    
    # invoke Action

    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph) -> {}:

        try:
            if Global._debug: print ("Add Action actionData:", actionData)
            if Global._debug: print ("Add Action dataDictionary:", dataDictionary)

            # "ADD <value> to <dictionary_variable>"

            value               = actionData[1] 
            dictionary_variable = actionData[3].upper()  

            if Global._debug: print ("Add Action:", value, "will be added to", dictionary_variable)

            dictionary_variable_value = int(dataDictionary[dictionary_variable]) + int(value)

            # Uupdate the data dictionary with the new value..

            dataDictionary.update({dictionary_variable : str(dictionary_variable_value)})

            return dataDictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerAddActionConstructC Exception:", e)
            raise e

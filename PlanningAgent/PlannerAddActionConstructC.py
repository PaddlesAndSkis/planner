# PlannerAddActionConstructC

# Import Project classes.

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA

# Import libraries.

import Global


class PlannerAddActionConstructC(PlannerGraphActionConstructA):
   
    def __init__(self):
        super().__init__()


    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph):

        print ("In ADD with", actionData)
        print ("In ADD with", dataDictionary)

        # "ADD <value> to <dictionary_variable>"

        value               = actionData[1] #.upper()  # .strip()
        dictionary_variable = actionData[3].upper()  #.delete('()').strip

        print ("In ADD with value to add to dictionary variable: ", value, "will be added to", dictionary_variable)


        dictionary_variable_value = int(dataDictionary[dictionary_variable]) + int(value)

        # Uupdate the data dictionary with the new value..

        dataDictionary.update({dictionary_variable : str(dictionary_variable_value)})

        return dataDictionary


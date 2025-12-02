# PlannerSetActionConstructC

from PlannerActionConstructA import PlannerActionConstructA
import Global

class PlannerSetActionConstructC(PlannerActionConstructA):
   
    # invokeAction

    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph) -> {}:

        try:

            if Global._debug: print ("Set Action actionData:", actionData)
            if Global._debug: print ("Set Action dataDictionary:", dataDictionary)

            myKey   = actionData[1].upper()  # .strip()
            myValue = actionData[3]  #.delete('()').strip

            if Global._debug: print ("Set Action:", myKey, "will be set to", myValue)

            dataDictionary[myKey] = myValue

            return dataDictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerSetActionConstructC Exception:", e)
            raise e

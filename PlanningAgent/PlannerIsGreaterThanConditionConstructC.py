# PlannerIsGreaterThanConditionConstructC

# Import libraries.

from PlannerConditionConstructA import PlannerConditionConstructA

import Global

class PlannerIsGreaterThanConditionConstructC(PlannerConditionConstructA):

    # Constructor.

    def __init__(self):

        pass
        #super.__init()


    # evaluate

    def evaluate(self, dataDictionary, conditionHash) -> bool:

        try:

            # Get the keyword-value from the condition Hash.

            myKey   = conditionHash["keyword"].upper()   # uppper case it
            myValue = conditionHash["value"]

            if Global._debug: print ("Is Greater THan Condition: testing if", myKey, ">", myValue)
            if Global._debug: print ("DataDictionary = ", dataDictionary)

            # Verify that the dictionary key exists so a key error does not occur.

            if (myKey in dataDictionary):
        
                dataDictionaryValue = dataDictionary[myKey]
                if Global._debug: print("Value for", myKey, "in the data dictionary is:", dataDictionaryValue)
                
                # Determine if there is a value for this key.

                if (dataDictionaryValue == None):
            
                    if (myValue == 'empty'):

                        return True
                    
                    else:
                        
                        return False

                else:

                    # Determine if the variable's value in the data dictionary is greater than the value
                    # specified in the condition.

                    if (int(dataDictionaryValue) > int(myValue)):

                        if Global._debug: print ("True:", dataDictionaryValue, ">", myValue)
                        
                        return True
                    
                    elif (myValue == 'empty') and (dataDictionaryValue == ""):
                        
                        if Global._debug: print ("False:", dataDictionaryValue, "=", myValue, "(empty)")
                        
                        return False

            # If this point is reached, the condition is False.

            if Global._debug: print ("False:", dataDictionaryValue, "<=", myValue)

            return False

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerIsGreaterThanConditionConstructC Exception:", e)
            raise e

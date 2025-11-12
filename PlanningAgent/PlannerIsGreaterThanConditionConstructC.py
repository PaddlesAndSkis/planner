# PlannerIsGreaterThanConditionConstructC

# Import libraries.

from PlannerConditionConstructA import PlannerConditionConstructA

class PlannerIsGreaterThanConditionConstructC(PlannerConditionConstructA):

    # Constructor.

    def __init__(self):

        pass
        #super.__init()



    def evaluate(self, dataDictionary, conditionHash):

        print("In PlannerIsGreaterThanConditionConstructC")

        # Get the keyword-value from the condition Hash.

        myKey   = conditionHash["keyword"].upper()   # uppper case it
        myValue = conditionHash["value"]

        print("KVP = >", myKey, "< ", myValue)

        # Get the value from the data dictionary.
        print("DataDictionary = ", dataDictionary)

        # Verify that the dictionary key exists so a key error does not occur.

        if (myKey in dataDictionary):
        
            dataDictionaryValue = dataDictionary[myKey]
            print("dataDictionaryValue =", dataDictionaryValue)

            if (dataDictionaryValue == None):
            
                if (myValue == 'empty'):
                    return True
                else:
                    return False

            else:

                print (dataDictionaryValue,">",myValue)

                if (int(dataDictionaryValue) > int(myValue)):
                    print ("GOOD!!")
                    return True
                elif (myValue == 'empty') and (dataDictionaryValue == ""):
                    print ("NOT GOOD!!")
                    return False

            print("KVP =", myKey, " ", myValue)

        return False

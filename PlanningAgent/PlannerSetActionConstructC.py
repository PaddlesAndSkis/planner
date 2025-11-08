# PlannerSetActionConstructC

from PlannerActionConstructA import PlannerActionConstructA
import Global

class PlannerSetActionConstructC(PlannerActionConstructA):
   
    def invokeAction(self, dataDictionary, actionData):

        print ("In SET with", actionData)
        print ("In SET with", dataDictionary)

        myKey   = actionData[1].upper()  # .strip()
        myValue = actionData[3]  #.delete('()').strip

        print ("In SET with myKey : myValue", myKey, " ->", myValue)

        dataDictionary[myKey] = myValue

        return dataDictionary


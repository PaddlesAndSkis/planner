# PlannerBooleanExpressionEvaluatorC.rb
#
# Concrete class for evaluating boolean expressions.

# Import libraries.

# Import Project classes.

import Global

from BooleanExpressionEvaluatorA import BooleanExpressionEvaluatorA
from PlannerIsConditionConstructC import PlannerIsConditionConstructC
from PlannerIsGreaterThanConditionConstructC import PlannerIsGreaterThanConditionConstructC
from PlannerIsLessThanConditionConstructC import PlannerIsLessThanConditionConstructC

# Class: PlannerBooleanExpressionEvaluatorC

class PlannerBooleanExpressionEvaluatorC(BooleanExpressionEvaluatorA):

    # Constructor
    #
    # [in]: booleanExpression - the boolean expression to evaluate
    # [in]: dataDictionary - the dictionary of variables (keyword-value pairs)

    def __init__(self, booleanExpression, dataDictionary):

        # Invoke the super class constructor.

        super().__init__(booleanExpression, dataDictionary)

        # Create a Hashtable of the set of allowable condition constructs.

        self.conditionConstructLibrary = {}
        self.conditionConstructLibrary["IS"]              = PlannerIsConditionConstructC()
        self.conditionConstructLibrary["IS_GREATER_THAN"] = PlannerIsGreaterThanConditionConstructC()
        self.conditionConstructLibrary["IS_LESS_THAN"]    = PlannerIsLessThanConditionConstructC()

 #       self.conditionConstructLibrary["CONTAINS"] = PlanterboxContainsConditionConstructC.new
 


    # evaluateConstruct
    #
    # Abstract method that is overridden by this concrete subclass.

    def evaluateConstruct(self):

        # api is finance     cam is_not here

        if Global._debug: print("LeftOperand =", self.leftOperand)

        constructComponents = self.leftOperand.split(" ", 3)

        print ("Construct components = ", constructComponents)

        subjectComponent = constructComponents[0].replace("(", "") 
        subjectComponent = subjectComponent.replace(")", "").strip() 
      
        verbComponent = constructComponents[1].upper().replace("(", "")
        verbComponent = verbComponent.replace(")", "").strip() 

        predicateComponent = constructComponents[2].replace("(", "")
        predicateComponent = predicateComponent.replace(")", "").strip()

        if Global._debug: print("subject:", subjectComponent)
        if Global._debug: print("verb:", verbComponent)
        if Global._debug: print("predicate:", predicateComponent)

        conditionHash = {}
        conditionHash["keyword"] = subjectComponent
        conditionHash["value"]   = predicateComponent

        print ("AM I HERE>>>>", conditionHash)

        return self.conditionConstructLibrary[verbComponent].evaluate(self.dataDictionary, conditionHash)


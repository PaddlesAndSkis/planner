# PlannerBooleanExpressionEvaluatorC.rb
#
# Concrete class for evaluating boolean expressions.

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


    # evaluateConstruct
    #
    # Abstract method that is overridden by this concrete subclass.

    def evaluateConstruct(self) -> bool:

        try:

            if Global._debug: print("LeftOperand =", self.leftOperand)

            # Split the token (leftOperand) into three parts: <subject> <verb> <predicate>

            constructComponents = self.leftOperand.split(" ", 3)

            if Global._debug: print ("Construct components = ", constructComponents)

            # Clean the subject component.

            subjectComponent = constructComponents[0].replace("(", "") 
            subjectComponent = subjectComponent.replace(")", "").strip() 
      
            # Clean the verb component.

            verbComponent = constructComponents[1].upper().replace("(", "")
            verbComponent = verbComponent.replace(")", "").strip() 

            # Clean the predicate component.

            predicateComponent = constructComponents[2].replace("(", "")
            predicateComponent = predicateComponent.replace(")", "").strip()

            if Global._debug: print("subject:", subjectComponent)
            if Global._debug: print("verb:", verbComponent)
            if Global._debug: print("predicate:", predicateComponent)

            # Create a dictionary consisting of a keyword-value pair with the
            # subject and predicate components.

            conditionHash = {}
            conditionHash["keyword"] = subjectComponent
            conditionHash["value"]   = predicateComponent

            # Return the boolean result (True or False) based on the evaluation of the condition.

            return self.conditionConstructLibrary[verbComponent].evaluate(self.dataDictionary, conditionHash)

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerBooleanExpressionEvaluatorC Exception:", e)
            raise e

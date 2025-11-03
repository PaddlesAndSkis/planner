# PlannerBooleanExpressionEvaluatorC.rb
#
# Concrete class for evaluating boolean expressions.

# Import libraries.

import "BooleanExpressionEvaluatorA.rb"
#import "Conditions/PlanterboxIsConditionConstructC.rb"
#import "Conditions/PlanterboxContainsConditionConstructC.rb"
#import "Conditions/PlanterboxLessThanConditionConstructC.rb"
#import "Conditions/PlanterboxGreaterThanConditionConstructC.rb"

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

        self.conditionConstructLibrary = []
 #       self.conditionConstructLibrary["IS"]   = PlanterboxIsConditionConstructC.new
 #       self.conditionConstructLibrary["CONTAINS"] = PlanterboxContainsConditionConstructC.new
 #       self.conditionConstructLibrary["LESSTHAN"] = PlanterboxLessThanConditionConstructC.new
 #       self.conditionConstructLibrary["GREATERTHAN"] = PlanterboxGreaterThanConditionConstructC.new
 


    # evaluateConstruct
    #
    # Abstract method that is overridden by this concrete subclass.

    def evaluateConstruct(self):

        # api is finance     cam is_not here

        if Global._debug: print("LeftOperand =", self.leftOperand)

        constructComponents = self.leftOperand.split(" ", 3)
        subjectComponent = constructComponents[0].delete('()').strip
        verbComponent = constructComponents[1].upcase.delete('()').strip
        predicateComponent = constructComponents[2].delete('()').strip

        if Global._debug: print("subject:", subjectComponent)
        if Global._debug: print("verb:", verbComponent)
        if Global._debug: print("predicate:", predicateComponent)

        conditionHash = []
        conditionHash["keyword"] = subjectComponent
        conditionHash["value"]   = predicateComponent

        return self.conditionConstructLibrary[verbComponent].evaluate(@dataDictionary, conditionHash)


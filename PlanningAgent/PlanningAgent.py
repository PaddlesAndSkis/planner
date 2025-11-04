
# PlanningAgent

# Import Project classes.
from PlannerBooleanExpressionEvaluatorC import PlannerBooleanExpressionEvaluatorC


def main():
    print ("Hello")

    condition = "[(cam is 55) AND (cam is westboro)] OR [(cam is 55) AND (cam is Ottawa)] ;"
    dataDictionary = {"CAM" : "55"}

    plannerBooleanExpressionEvaluator = PlannerBooleanExpressionEvaluatorC(condition, dataDictionary)
    conditionBooleanResult = plannerBooleanExpressionEvaluator.evaluateBooleanExpression()

# Start the Agent.

main()
# BooleanExpressionEvaluatorA.rb
#
# Abstract class for evaluating boolean expressions.

# Import libraries.

from abc import ABC, abstractmethod
import re

# Import Project classes.

import Global


# Class: BooleanExpressionEvaluatorA

class BooleanExpressionEvaluatorA(ABC):

    # Define attributes.

  #  attr_accessor  :booleanExpression, :dataDictionary, :postToken, :leftOperand, :currentTokenIndex

    # Constructor
    #
    # [in]: booleanExpression - the boolean expression to evaluate
    # [in]: dataDictionary - the dictionary of variables (keyword-value pairs)

    def __init__(self, booleanExpression, dataDictionary):
    
        try:

            self.booleanExpression = []

            if Global._debug: print ("boolean expression: ", booleanExpression)

            # Split the boolean expression based the language constructs.

            self.tempExpression = re.split(r"([\!\[\]\(\)])", booleanExpression)

            #self.tempExpression = booleanExpression.split(/(?<=[\!\[\]\)])/).map(&:strip)

            if Global._debug: print ("Parsed boolean expression", self.tempExpression)

            # Iterate over the tokens in the expression and only keep the ones that are necessary.
            # In other words, no empty strings or the brackets '()'.

            for token in self.tempExpression:

                token = token.strip()
           
                if (len(token) == 0):
                    continue

                if (token in '()'):
                    continue

                self.booleanExpression.append(token)

            if Global._debug: print ("Parsed boolean expression", self.booleanExpression)

            self.dataDictionary = dataDictionary
            self.postToken = ""
            self.leftOperand = ""
            self.currentTokenIndex = -1

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("BooleanExpressionEvaluatorA Exception:", e)
            raise e

    
    # evaluateBooleanExpression

    def evaluateBooleanExpression(self):

        try:

            leftBoolResult = False

            leftBoolResult = self.evaluateOrExpression()

            # Determine if the end of line character has been reached.

            if (self.postToken == ";"):

                # It has, therefore return the result of the boolean expression.

                return leftBoolResult

            else:

                # Otherwise, the end of line expression is missing.

                raise Exception("ERROR: missing end of boolean expression token - ; in", self.booleanExpression)

            return False

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("BooleanExpressionEvaluatorA Exceptijjon:", e)
            raise e


    # Private methods


    # evaluateOrExpression

    def evaluateOrExpression(self):

        try:

            # Set the left and right condition boolean result indicators.

            leftBoolResult = False
            rightBoolResult = False 

            # Get the left condition boolean result for the AND condition
            # as AND takes precedence over OR.

            leftBoolResult = self.evaluateAndExpression()

            # Do while the OR condition.

            while (self.postToken == "OR"):

                # Evaluate the AND condition.

                rightBoolResult = self.evaluateAndExpression()

                # Determine if the OR condition is True or False.
                # (T | F) = T; T | T = T etc.

                if ((leftBoolResult == True) or (rightBoolResult == True)):

                    leftBoolResult = True
                else:

                    leftBoolResult = False

            
            # Return the left boolean condition result.

            return leftBoolResult

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("BooleanExpressionEvaluatorA Exception:", e)
            raise e


    # evaluateAndExpression

    def evaluateAndExpression(self):

        try:

        # Set the left and right condition boolean result indicators.

            leftBoolResult = False
            rightBoolResult = False 

            # Evaluate the sub condition to get the left boolean
            # result.

            leftBoolResult = self.evaluateSubCondition()

            # Is the token an AND.

            while (self.postToken == "AND"):

                # Evaluate the AND condition expression.

                rightBoolResult = self.evaluateAndExpression()

                # Determine if the AND condition is True or False.
                # (T & F) = F; T & T = T etc.
                
                if ((leftBoolResult == True) and (rightBoolResult == True)):

                    leftBoolResult = True
                else:

                    leftBoolResult = False

            # Return the left boolean condition result.

            return leftBoolResult

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("BooleanExpressionEvaluatorA Exception:", e)
            raise e


    # evaluateSubCondition

    def evaluateSubCondition(self):

        try:

            # Set the boolean indicators.

            leftBoolResult = False
            isNotExpression = False

            # Get the next token in the expression.

            self.leftOperand = self.nextTokenInExpression()

            # Determine if this is a NOT (!) operation.

            if (self.leftOperand == "!"):

                # It is a NOT (!) operation.

                isNotExpression = True
                self.leftOperand = self.nextTokenInExpression()

  
            # Determine if this is a left bracket for order of operations.

            if (self.leftOperand == "["):

                # It is a left bracket, therefore start by evaluating the
                # OR expression.

                leftBoolResult = self.evaluateOrExpression()

                # Determine if the next token is the right bracket to end 
                # an order of operations expression.

                if (self.postToken == "]"):

                    # This is the end of the expression.  Determine if this 
                    # was a NOT (!) expression.

                    if (isNotExpression == True): 

                        # This is a NOT (!) expression, therefore, return
                        # the opposite result.

                        if (leftBoolResult == True):

                            # Reverse the boolean result.

                            leftBoolResult = False

                        else:
                        
                            # Same as above, reverse the boolean result as
                            # this is a NOT (!) expression.

                            leftBoolResult = True

                        # Reset the NOT (!) expression indicator.

                        isNotExpression = False

                    # Get the next token in the expression.

                    self.postToken = self.nextTokenInExpression()
                
                else:

                    # If this point is reached, a right parenthesis is missing and 
                    # therefore, the expression is misformed.

                    print ("ERROR: Received", self.postToken, "Missing right parenthesis in", self.booleanExpression)
                    raise Exception("ERROR: Received", self.postToken, "Missing right parenthesis in", self.booleanExpression)
               
            else:

                # Evaluate the condition.

                expressionResult = self.evaluateConstruct()

                if Global._debug: print(self.leftOperand, "is", expressionResult)

                # Set the boolean result.
                
                if (expressionResult == True):

                    self.postToken = self.nextTokenInExpression()
                    leftBoolResult = True

                else:
                   
                    self.postToken = self.nextTokenInExpression()
                    leftBoolResult = False

            # Return the boolean result.

            return leftBoolResult

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("BooleanExpressionEvaluatorA Excepiiition:", e)
            raise e

        
    # nextTokenInExpression

    def nextTokenInExpression(self):

        try:

            needAToken = True

            while (needAToken == True):

                self.currentTokenIndex = self.currentTokenIndex + 1

              #  print ("currentTokenIndex = ", self.currentTokenIndex)
              #  print ("self.booleanExpression = ", self.booleanExpression)

                i = 0
                for toke in self.booleanExpression:
                #    print (i, ' ', self.booleanExpression[i]);
                    i = i + 1

                currentToken = self.booleanExpression[self.currentTokenIndex]

                if Global._debug: print("Evaluating expression token:", currentToken)

                if (currentToken != ""):

                    needAToken = False

            return currentToken

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("BooleanExpressionEvaluatorA Exception:", e)
            raise e

        
    # evaluateConstruct
    #
    # Abstract method that needs to be overridden by a concrete subclass.
    # Note, you cannot use the prefix "__" for an abstract method.

    @abstractmethod
    def evaluateConstruct(self) -> bool:

        # Display an error message.

        if Global._debug: print("BooleanExpressionEvaluatorA is an abstract class.")





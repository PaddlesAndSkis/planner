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
    
        self.booleanExpression = []

        print ("boolean expression: ", booleanExpression)

        # Split the boolean expression based the language constructs.

        self.tempExpression = re.split(r"([\[\!\]\);])", booleanExpression)

        #self.tempExpression = booleanExpression.split(/(?<=[\!\[\]\)])/).map(&:strip)
       # self.tempExpression = re.split(r"/(?<=[\!\[\]\)])/", booleanExpression)

       # pattern_literal_brackets = r'/([\!\[\]\)])/'
       # self.tempExpression = re.split(pattern_literal_brackets, booleanExpression)
#match = re.search(r'word:\w\w\w', str)
#re.sub(r"\.\[\d+\]",'',value)

       # text = "This is [data] in brackets."
        # Matches the literal '[' and ']' characters
       # pattern_literal_brackets = r'\[|\]'
       # matches_literal_brackets = re.findall(pattern_literal_brackets, text)
       # print(matches_literal_brackets)


        print ("tempExpression = ", self.tempExpression)

      #  s = "apple,banana;cherry grapes"

      #  print ("Testing s: ", s)
        # Split by comma, semicolon, or space
      #  self.tempExpression = re.split(r"([\[\!\];])", booleanExpression)
      #  print(self.tempExpression)

        if Global._debug: print ("Parsed boolean expression", self.tempExpression)

        # Iterate over the tokens in the expression.

        for token in self.tempExpression:

            token = token.strip()

            if (len(token) == 0):
                print("NIL => moving on")
                next

            if Global._debug: print("Token:", token, len(token))
           
            # Determine if the token is an AND or OR.

            if (token.upper().startswith("AND")):   # Add upper case

                # AND clause.
                print ("!!!! AND")

                self.booleanExpression.append("AND")
            #    token = (token.split("AND", 2).map(&:strip))[1]
                token = re.split("AND", token)[1]
                print ("TOKEN AFTER AND:", token)

            elif (token.upper().startswith("OR")):   # Add upper case

                # OR clause.

                print ("!!!! OR")
                self.booleanExpression.append("OR")
             #   token = (token.split("OR", 2).map(&:strip))[1]
                token = re.split("OR", token)[1]
                print ("TOKEN AFTER OR:", token)

            elif (token == ')'):
                next

            self.booleanExpression.append(token)

        print ("booleanExpression=", self.booleanExpression)

        self.dataDictionary = dataDictionary
        self.postToken = ""
        self.leftOperand = ""
        self.currentTokenIndex = -1



    
    # evaluateBooleanExpression

    def evaluateBooleanExpression(self):

        print ("FDDFDJKFJKFJDKFD")
        leftBoolResult = False

        leftBoolResult = self.evaluateOrExpression()
        print ("!!!!!!!!!!!!evaluateBooleanExpression -> self.postToken", self.postToken)

        # Determine if the end of line character has been reached.

        if (self.postToken == ";"):

            # It has, therefore return the result of the boolean expression.

            return leftBoolResult

        else:

            # Otherwise, the end of line expression is missing.

            # raise "ERROR: missing end of boolean expression token - ; in #{@booleanExpression}"
            print ("ERROR: missing end of boolean expression token - ; in", self.booleanExpression)

        return False


    # Private methods

    #protected

    # evaluateOrExpression

    def evaluateOrExpression(self):

        # Set the left and right condition boolean result indicators.

        leftBoolResult = False
        rightBoolResult = False 

        # Get the left condition boolean result for the AND condition
        # as AND takes precedence over OR.

        leftBoolResult = self.evaluateAndExpression()
        print ("!!!!!!!!!!evaluateOrExpression -> self.postToken", self.postToken)

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


    # evaluateAndExpression

    def evaluateAndExpression(self):

        # Set the left and right condition boolean result indicators.

        leftBoolResult = False
        rightBoolResult = False 

        # Evaluate the sub condition to get the left boolean
        # result.

        leftBoolResult = self.evaluateSubCondition()
        print ("!!!!!!!!!!!!evaluateAndExpression -> self.postToken", self.postToken)

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


    # evaluateSubCondition

    def evaluateSubCondition(self):

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

  
        print ("Self.leftOperand = ", self.leftOperand)
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

                    #raise "ERROR: Missing right parenthesis in #{@booleanExpression}"
                    if Global._debug: print("ERROR: Missing right parenthesis in", self.booleanExpression)

               
            else:

                # Evaluate the condition.

                expressionResult = self.evaluateConstruct()

                if Global._debug: print(self.booleanExpression, "is", expressionResult)

                # Set the boolean result.
                
                if (expressionResult == True):

                    self.postToken = self.nextTokenInExpression()
                    leftBoolResult = True

                else:
                   
                    self.postToken = self.nextTokenInExpression()
                    leftBoolResult = False

        # Return the boolean result.

        return leftBoolResult
        

    # nextTokenInExpression

    def nextTokenInExpression(self):

        needAToken = True

        while (needAToken == True):

            self.currentTokenIndex = self.currentTokenIndex + 1
            currentToken = self.booleanExpression[self.currentTokenIndex]

            if Global._debug: print("Evaluating expression token:", currentToken)

            if (currentToken != ""):

                needAToken = False

        return currentToken
        

    # evaluateConstruct
    #
    # Abstract method that needs to be overridden by a concrete subclass.

    @abstractmethod
    def evaluateConstruct():
        if Global._debug: print("BooleanExpressionEvaluatorA is an abstract class.")





# PlannerControllerC

import re

# Import Project classes.

import Global

from PlannerBooleanExpressionEvaluatorC import PlannerBooleanExpressionEvaluatorC
from PlannerActionEvaluatorConstructC import PlannerActionEvaluatorConstructC
from PlannerKnowledgeGraphC import PlannerKnowledgeGraphC
from KnowledgeBaseC import KnowledgeBaseC



class PlannerControllerC:

    # Constructor

    def __init__(self, agent, environment):

        # Set the Agent and Environment.

        self.agent = agent
        self.environment = environment


    # start_agent

    def start_agent(self):

        # Start the Agent with the environment in which it is operating.

        self.agent.agent_goes_to_work(self.environment)


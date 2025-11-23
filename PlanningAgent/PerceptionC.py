# PerceptionC

# Import Project classes.

import Global


class PerceptionC:

    # Constructor

    def __init__(self, environment):

        # Responsible for interacting with the environment to get the
        # percepts or other inputs.

        self.environment = environment


    # gather_inputs_from_environment

    def gather_inputs_from_environment(self) -> []:

        return self.environment.get_environment_input()

    
    # get_plan_from_user

    def get_plan_from_user(self) -> str:

        # Get the plan from the user.

        print ("\n\n------------")
        print ("The following plans are available:", Global._plan_list)
        return input("Please enter a plan to retrieve: ")

        





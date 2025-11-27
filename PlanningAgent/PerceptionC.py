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

        while (True):

            print ("\n\n------------")
            print ("The following plans are available:", Global._plan_list)
            plan = input("Please enter a plan to retrieve: ").strip().lower()

            # Ensure the plan is valid or is "Quit".

            if (plan in Global._plan_list):

                return plan

            else:

                print ("Plan", plan, "is not valid.  Please select a plan or Quit to exit.")

        

        





# PlannerControllerC


class PlannerControllerC:

    # Constructor

    def __init__(self, agent, environment):

        # Set the Agent and Environment.

        self.agent = agent
        self.environment = environment


    # start_agent

    def start_agent(self):

        try:

            # Start the Agent with the environment in which it is operating.

            self.agent.agent_goes_to_work(self.environment)

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerController Exception:", e) 
            raise e

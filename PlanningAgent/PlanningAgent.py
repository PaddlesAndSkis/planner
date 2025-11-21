# PlanningAgent

# Import Project classes.

import Global

from AgentC import AgentC
from EnvironmentC import EnvironmentC
from PlannerControllerC import PlannerControllerC

# main - Application Main Driver

def main():

    try:

        if Global._info: print ("Starting the Agent Planning Session")

        # Create the Agent and Environment.

        agent = AgentC()
        environment = EnvironmentC("APM", "my_data_file.xlsx", "Planner_Rules.json")

        # Setup the Planner Controller with the Agent and Environment.

        planner_controller = PlannerControllerC(agent, environment)

        # Start the Agent.

        planner_controller.start_agent()

        # At this point, the Agent Planning session is complete.
   
        if Global._info: print ("Agent Planning Session complete.")

    except Exception as e:

        # Catch and log all exceptions.

        print ("PlanningAgent Exception:", e)


# Start the Agent Planning Session.

main()
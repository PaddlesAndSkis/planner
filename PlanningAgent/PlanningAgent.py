# PlanningAgent

# Import Project classes.

from AgentC import AgentC
from EnvironmentC import EnvironmentC
from PlannerControllerC import PlannerControllerC

# main - Application Main Driver

def main():

    print ("Starting the Agent Planning Session")

    # Create the Agent and Environment.

    agent = AgentC()
    environment = EnvironmentC("APM", "my_data_file.xlsx", "Planner_Rules.json")

    # Setup the Planner Controller with the Agent and Environment.

    planner_controller = PlannerControllerC(agent, environment)

    # Start the Agent.

    planner_controller.start_agent()

    # At this point, the Agent Planning session is complete.
   
    print ("Agent Planning Session complete.")


# Start the Agent Planning Session.

main()
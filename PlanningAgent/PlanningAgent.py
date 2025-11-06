
# PlanningAgent

# Import Project classes.

from AgentC import AgentC
from EnvironmentC import EnvironmentC
from PlannerControllerC import PlannerControllerC


def main():

    print ("Starting the Agent Planning Session")

    my_agent = AgentC()
    my_environment = EnvironmentC("APM", "my_data_file.xlsx", "apm_rules.json")

    planner_controller = PlannerControllerC(my_agent, my_environment)

    planner_controller.start_planning_session()
   
    print ("Agent Planning Session complete.")


# Start the Agent Planning Session.

main()
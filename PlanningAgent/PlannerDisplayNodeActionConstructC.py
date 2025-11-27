# PlannerDisplayNodeActionConstructC

# Import Project classes.

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA
import Global


# Import libraries.

import re


class PlannerDisplayNodeActionConstructC(PlannerGraphActionConstructA):
   
    # Constructor

    def __init__(self):

        super().__init__()


    # invokeAction

    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph) -> {}:

        try:

            if Global._debug: print ("Display_Node Action actionData:", actionData)
            if Global._debug: print ("Display_Node Action dataDictionary:", dataDictionary)

            # "DISPLAY_PLAN application on node low_business_value+high_technical_condition+high_application_cost"
            # "DISPLAY_PLAN application on node shortest_path"

            plan_name        = actionData[1] #.upper()  # .strip()
            attribute_name   = actionData[2] #.upper()  # .strip()
            node_name        = actionData[5]  #.delete('()').strip

            if Global._debug: print ("Display_Node Action:", attribute_name, " on Node named", node_name)

            if Global._debug: plannerKnowledgeGraph.print()

            # Determine which information to display.

            if (node_name == 'shortest_path'):

                self.display_shortest_path(plannerKnowledgeGraph)

            elif (node_name == 'longest_path'):

                self.display_longest_path(plannerKnowledgeGraph)

            else:

                self.display_node_via_search(plan_name, node_name, plannerKnowledgeGraph)

            return dataDictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerDisplayNodeActionConstructC Exception:", e)
            raise e


    # display_shortest_path

    def display_shortest_path(self, plannerKnowledgeGraph):

        # Retrieve the shortest path nodes from the graph.

        shortest_path_nodes = plannerKnowledgeGraph.get_shortest_path_nodes()

        # Display the shortest path.

        if Global._debug: print ("Shortest path through the graph:", shortest_path_nodes)

        # Pop the shortest path nodes to remove the End node.

        shortest_path_nodes.pop()

        # Get the last leaf node which will contain all the entities that made it to the last node.

        last_leaf_node = shortest_path_nodes.pop()

        entities = plannerKnowledgeGraph.get_node_applications(last_leaf_node, "application")

        print ("Entities:", entities) if (len(entities) > 0) else print ("This plan does not have any entities.")


    # display_longest_path

    def display_longest_path(self, plannerKnowledgeGraph):

        # Retrieve the shortest path nodes from the graph.

        longest_path_nodes = plannerKnowledgeGraph.get_longest_path_nodes()

        # Display the longest path.

        if Global._debug: print ("Longest path through the graph:", longest_path_nodes)

        # Pop the shortest path nodes to remove the End node.

        longest_path_nodes.pop()

        # Get the last leaf node which will contain all the entities that made it to the last node.

        last_leaf_node = longest_path_nodes.pop()

        entities = plannerKnowledgeGraph.get_node_applications(last_leaf_node, "application")

        print ("Entities:", entities) if (len(entities) > 0) else print ("This plan does not have any entities.")


    # display_node_via_search

    def display_node_via_search(self, plan_name, search_criteria, plannerKnowledgeGraph) -> {}:

        try:

            # Print out the plan name.

            print ("PLAN:", plan_name)

            matched_nodes_list = []
            search_criteria_tokens =  re.split(r"\+", search_criteria)

            if Global._debug: print ("Search criteria", search_criteria)
            if Global._debug: print ("Search criteria tokens", search_criteria_tokens)

            final_nodes_list = plannerKnowledgeGraph.search_graph_by_multi_names(search_criteria_tokens, matched_nodes_list)

            if Global._debug: print ("Final nodes list = ", final_nodes_list)
            if Global._debug: print ("Final nodes list sorted = ", sorted(final_nodes_list))

            final_entities_list = []

            for final_node in final_nodes_list:

                entities = plannerKnowledgeGraph.get_node_applications(final_node, "application")

                final_entities_list.append(entities)

            print ("PLAN:", plan_name)
            print ("------------------")
            print ("The final application list for plan,", plan_name, "is:\n\n", final_entities_list) if (len(final_entities_list) > 0) else print ("This plan does not have any entities.")
        
        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerDisplayNodeActionConstructC Exception:", e)
            raise e
        

        #planner_knowledge_graph.print_node_applications("1.1.1.1", "application")
        #planner_knowledge_graph.print_leaf_nodes("application")
        #planner_knowledge_graph.add_end_node()
        
        #planner_knowledge_graph.print()

        #print("If you know the name of the node, you can iterate through all the nodes and get the name:")
        #planner_knowledge_graph.search_graph_by_name("Low_business_value")
        #planner_knowledge_graph.search_graph_by_name("Low_technical_condition")

        #print("If you want to know which nodes have Low_business_value, Low_technical_condition, you must BFS:")
        #planner_knowledge_graph.search_graph_by_names('Low_business_value', 'Low_technical_condition')

        #print("If you want to get all the edges in a breadth first search:")
        #planner_knowledge_graph.breadth_first_search('Start')

        #print("Applications that should be Tolerated")
        #print("-------------------------------------")
        #print("The following applications have a low business value and a high technical condition, you must BFS:")
        #planner_knowledge_graph.search_graph_by_names('Low_business_value', 'Low_technical_condition')
        
        #print("If you want to know which nodes have high application risk, low modernization, you must BFS:")
        #planner_knowledge_graph.search_graph_by_names('High_application_risk', 'Low_modernization')

        #planner_knowledge_graph.print_node_applications("1", "application")
        #planner_knowledge_graph.print_node_applications("2", "application")


        # Application Rationalization Plan
        #----------------------------------
        # 1. Focus on the applications as they have scored the lowest:
        #
        #       - App1
        #       - App2

        # 2. These applications can be easily decommissioned as they have low business and technical value:

        # 3. These applications will save you the most money as they have high application cost and low business value

        # 4. These applications may be quite risky to remove as they have a high application risk.

        # 5.  These applications scored the best so they can be prioritized at the bottom of the list.

        #  Here are some charts:

        #  Here is the graph that was built to explore


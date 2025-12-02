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

            plan_name        = actionData[1] 
            attribute_name   = actionData[2] 
            node_name        = actionData[5] 

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

        print (entities) if (len(entities) > 0) else print ("This plan does not have any entities.")


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

        print (entities) if (len(entities) > 0) else print ("This plan does not have any entities.")


    # display_node_via_search

    def display_node_via_search(self, plan_name, search_criteria, plannerKnowledgeGraph) -> {}:

        try:

            # Print out the plan name.

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
            print ("The final list for plan,", plan_name, ", is:\n\n", final_entities_list) if (len(final_entities_list) > 0) else print ("This plan does not have any entities.")

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerDisplayNodeActionConstructC Exception:", e)
            raise e
        

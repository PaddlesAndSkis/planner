# PlannerDisplayNodeActionConstructC

# Import Project classes.

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA

# Import libraries.

import Global


class PlannerDisplayNodeActionConstructC(PlannerGraphActionConstructA):
   
    def __init__(self):
        super().__init__()


    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph):

        print ("In DISPLAY_NODE with", actionData)
        print ("In DISPLAY_NODE with", dataDictionary)

        # "DISPLAY_PLAN application on node low_business_value+high_technical_condition+high_application_cost"
        # "DISPLAY_PLAN application on node shortest_path"

        attribute_name  = actionData[1] #.upper()  # .strip()
      #  attribute_value = actionData[2] #.upper()  # .strip()
        node_name         = actionData[4]  #.delete('()').strip

        print ("In DISPLAY_NODE with", attribute_name, " on Node named", node_name)

        # Display the information on the node to the Planner Knowledge Graph.

        plannerKnowledgeGraph.print()
        plannerKnowledgeGraph.print_shortest_path()

        print("If you want to know which nodes have Low_business_value, Low_technical_condition, you must BFS:")
        plannerKnowledgeGraph.search_graph_by_names('Low_business_value', 'Low_technical_condition')

        return dataDictionary



        #planner_knowledge_graph.print_node_applications("1.1.1.1", "application")
        #planner_knowledge_graph.print_leaf_nodes("application")
        #planner_knowledge_graph.add_end_node()
        
        #planner_knowledge_graph.print()
        #planner_knowledge_graph.print_shortest_path()
        #planner_knowledge_graph.print_longest_path()

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


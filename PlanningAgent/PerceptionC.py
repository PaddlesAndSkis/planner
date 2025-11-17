# PerceptionC

# Import Project classes.

from KnowledgeBaseC import KnowledgeBaseC


class PerceptionC:

    # Constructor

    def __init__(self, kb):

        # Responsible for the query input
        # Parsing the input
        # Tokenize input

        self.kb = kb


    # invoke_plans

    def invoke_plans(self):

        # Get the Planner Knowledge Graph.

        planner_knowledge_graph = self.kb.get_knowledge_graph()

        # e.g.:
        # self.perception.set_knowledge_graph(planner_knowledge_graph)

        planner_knowledge_graph.print_node_applications("1.1.1.1", "application")
        planner_knowledge_graph.print_leaf_nodes("application")
        planner_knowledge_graph.add_end_node()
        
        planner_knowledge_graph.print()
        planner_knowledge_graph.print_shortest_path()
        planner_knowledge_graph.print_longest_path()

        print("If you know the name of the node, you can iterate through all the nodes and get the name:")
        planner_knowledge_graph.search_graph_by_name("Low_business_value")
        planner_knowledge_graph.search_graph_by_name("Low_technical_condition")

        print("If you want to know which nodes have Low_business_value, Low_technical_condition, you must BFS:")
        planner_knowledge_graph.search_graph_by_names('Low_business_value', 'Low_technical_condition')

        print("If you want to get all the edges in a breadth first search:")
        planner_knowledge_graph.breadth_first_search('Start')

        print("Applications that should be Tolerated")
        print("-------------------------------------")
        print("The following applications have a low business value and a high technical condition, you must BFS:")
        planner_knowledge_graph.search_graph_by_names('Low_business_value', 'Low_technical_condition')
        
        print("If you want to know which nodes have high application risk, low modernization, you must BFS:")
        planner_knowledge_graph.search_graph_by_names('High_application_risk', 'Low_modernization')

        planner_knowledge_graph.print_node_applications("1", "application")
        planner_knowledge_graph.print_node_applications("2", "application")


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




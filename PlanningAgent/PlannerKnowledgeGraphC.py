# PlannerKnowledgeGraphC

# Import Project classes.

import Global

# Import libraries.

import networkx as nx

class PlannerKnowledgeGraphC:

    # Constructor

    def __init__(self):
        self.G = nx.DiGraph()
        self.G.add_node("Start", node="Start", application="n/a")


    def add_node(self, node_id, node_name, attribute_name, attribute_value):

        # "ADD_NODE <attribute_name> <attribute_value> to <node_id> named <node_name>"

        attribute_list = [] 
        
        print ("attribute_list  = ", attribute_list)
        print ("attribute_name  = ", attribute_name)
        print ("attribute_value = ", attribute_value)
        if (self.G.has_node(node_id)):

            attribute_list = list(self.G.nodes[node_id][attribute_name])
            print ("aaaattribute_list  = ", attribute_list)
        
        attribute_list.append(attribute_value)

        self.G.add_node(node_id, node=node_id, name=node_name)
        self.G.nodes[node_id][attribute_name] = attribute_list


    def add_edge(self, current_node, dest_node, weight):

        # "ADD_EDGE $dest_node$ to $current_node$ weighted $weight$

        self.G.add_edge(current_node, dest_node, weight=int(weight))

    def add_end_node(self):

        leaf_nodes = [node for node in self.G.nodes() if self.G.out_degree(node) == 0]

        for leaf_node in leaf_nodes:
            
            self.add_edge(leaf_node, "End", 0)

    def print_node_applications(self, node_id, attribute_name):

        print ("Node ", node_id, "is named", self.G.nodes[node_id]["name"], "and contains attributes:", self.G.nodes[node_id][attribute_name])

    def print_leaf_nodes(self, attribute_name):

        leaf_nodes = [node for node in self.G.nodes() if self.G.out_degree(node) == 0]

        print ("leaf nodes:", leaf_nodes)

        for leaf_node in leaf_nodes:
            self.print_node_applications(leaf_node, attribute_name)


    def print_shortest_path(self):

        source_node = "Start"
        dest_node = "End"

        if Global._debug: print ("\nShortest Dijkstra path:", nx.shortest_path(self.G, source_node, dest_node, weight=None, method='dijkstra'))
        if Global._debug: print ("\nShortest A* path:", nx.astar_path(self.G, source_node, dest_node, heuristic=None, weight='manhattan_distance'))
        if Global._debug: print ("\nShortest path by weight:", nx.shortest_path(self.G, source_node, dest_node, weight='weight'))
        if Global._debug: print ("\nShortest path length:", nx.shortest_path_length(self.G, source_node, dest_node, weight='weight'))

    def print_longest_path(self):

        if Global._debug: print ("\nLongest path:", nx.dag_longest_path(self.G, weight='weight'))

    def print(self):

        print("!!!! NODES:", self.G.nodes)
        print("!!!! EDGES:", self.G.edges)


    def breadth_first_search(self, source_node):
        
        graph_edges = list(nx.bfs_edges(self.G, source_node))

        print ("BFS Edges:", graph_edges)

        return graph_edges


    def search_graph_by_name(self, node_name):

        for node_id, attributes in self.G.nodes(data=True):
            
            if (attributes.get('name') == node_name):

                print ("Node_id", node_id, "is named", node_name, "and contains apps", attributes['application'])


    def search_graph_by_names(self, node_name1, node_name2):

        matched_nodes_list = []
        both_matched_nodes_list = []
        # Get the list of bread_first_search edges.

        graph_edges = self.breadth_first_search('Start')

        for u, v in graph_edges:

            print ("v = ", v)
            if (self.G.nodes[v].get("name") == node_name1):

                matched_nodes_list.append(v)

        print ("Matched_nodes_list = ", matched_nodes_list)
            
        for matched_node in matched_nodes_list:

            matched_graph_edges = self.breadth_first_search(matched_node)

            for u, v in matched_graph_edges:

                print ("v = ", v)
                if (self.G.nodes[v].get("name") == node_name2):

                    both_matched_nodes_list.append(v)


        print ("Both Matched_nodes_list = ", both_matched_nodes_list)

        print ("The applications that")


#    node_list = [ 'Low_business_value', 'High_technical_condition', 'Low_application_risk']
#    matched_nodes_list = []
    def search_graph_by_multi_names(self, node_list, matched_nodes_list) -> []:

        print ("MULTI node_list", node_list)
        print ("MULTI matched_nodes_list", matched_nodes_list)

        if (len(node_list) > 0):
            node_to_match = node_list.pop()
            print ("MULTI node_to_match", node_to_match)
        else:
            return matched_nodes_list

        graph_edges = self.breadth_first_search('Start')

        for u, v in graph_edges:

            print ("v = ", v)
            if (self.G.nodes[v].get("name") == node_to_match):

           #     if (v not in matched_nodes_list):
                matched_nodes_list.append(v)

        # matched_nodes_list = ['1', '1.2']

        print ("MULTI now matched_nodes_list", matched_nodes_list)

     #   for matched_node in matched_nodes_list:

     #       print ("MULTI now node_list", node_list)
      #      print ("MULTI now matched_nodes_list", matched_nodes_list)

        return self.search_graph_by_multi_names(node_list, matched_nodes_list)


    def find_path_through_graph(self, node_list):

        for source_node in node_list:

            for target_node in node_list:

                if (source_node != target_node):

                    path_exists = nx.has_path(self.G, source=source_node, target=target_node)
                    print(f"Path exists between {source_node} and {target_node}: {path_exists}")

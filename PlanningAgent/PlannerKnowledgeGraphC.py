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


    def add_node(self, node_id, node_name, application):

        # "ADD_NODE <application> to <node_id> named <node_name>"
        applications = []
        
        if (self.G.has_node(node_id)):

            applications = self.G.nodes[node_id]["application"]
        
        applications.append(application)

        self.G.add_node(node_id, node=node_id, name=node_name, application=applications)


    def add_edge(self, current_node, dest_node, weight):

        # "ADD_EDGE $dest_node$ to $current_node$ weighted $weight$

        self.G.add_edge(current_node, dest_node, weight=int(weight))

    def add_end_node(self):

        leaf_nodes = [node for node in self.G.nodes() if self.G.out_degree(node) == 0]

        for leaf_node in leaf_nodes:
            
            self.add_edge(leaf_node, "End", 0)

    def print_node_applications(self, node_id):

        print ("Node ", node_id, "is named", self.G.nodes[node_id]["name"], "and contains applications:", self.G.nodes[node_id]['application'])

    def print_leaf_nodes(self):

        leaf_nodes = [node for node in self.G.nodes() if self.G.out_degree(node) == 0]

        print ("leaf nodes:", leaf_nodes)

        for leaf_node in leaf_nodes:
            self.print_node_applications(leaf_node)


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


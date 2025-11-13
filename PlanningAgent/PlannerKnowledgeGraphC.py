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


    def add_node(self, node_name, application):

        # "ADD_NODE $application$ to TC-$technical_condition$"
        applications = []
        
        if (self.G.has_node(node_name)):

            applications = self.G.nodes[node_name]["application"]
        
        applications.append(application)

        self.G.add_node(node_name, node=node_name, application=applications)


    def add_edge(self, current_node, dest_node, weight):

        # "ADD_EDGE $dest_node$ to $current_node$ weighted $weight$

        self.G.add_edge(current_node, dest_node, weight=int(weight))

    def add_end_node(self):

        leaf_nodes = [node for node in self.G.nodes() if self.G.out_degree(node) == 0]

        for leaf_node in leaf_nodes:
            
            self.add_edge(leaf_node, "End", 0)

    def print_node_applications(self, node_name):

        print ("Node ", node_name, "contains applications:", self.G.nodes[node_name]['application'])

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



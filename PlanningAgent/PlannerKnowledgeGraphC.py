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


    # add_node

    def add_node(self, node_id, node_name, attribute_name, attribute_value):

        try:

            attribute_list = [] 
        
            if Global._debug: print ("PlannerKnowledgeGraphC add_node attribute_list  = ", attribute_list)
            if Global._debug: print ("PlannerKnowledgeGraphC add_node attribute_name  = ", attribute_name)
            if Global._debug: print ("PlannerKnowledgeGraphC add_node attribute_value = ", attribute_value)

            # Check to see if a node with this node_id already exists in the graph.

            if (self.G.has_node(node_id)):

                # This node already exists.  Therefore, get the node's attribute specified
                # by the attribute name.

                attribute_list = list(self.G.nodes[node_id][attribute_name])
                if Global._debug: print ("Node", node_id, " ", attribute_name, "is:", attribute_list)
        
            # Append the new attribute value to the attribute list.

            attribute_list.append(attribute_value)

            # Add the node and its attribute list.

            self.G.add_node(node_id, node=node_id, name=node_name)
            self.G.nodes[node_id][attribute_name] = attribute_list
            self.G.nodes[node_id]["description"] = attribute_list

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerKnowledgeGraphC Exception:", e)
            raise e


    # add_edge

    def add_edge(self, current_node, dest_node, weight):
        
        # Add an edge between the source node and destination node.
        # Add the weight.


        self.G.add_edge(current_node, dest_node, weight=int(weight))

    
    # add_end_node

    def add_end_node(self):

        # Get all of the leaf nodes in the graph.

        leaf_nodes = [node for node in self.G.nodes() if self.G.out_degree(node) == 0]

        # Iterate through the leaf nodes and add an edge to the End node.

        for leaf_node in leaf_nodes:
            
            self.add_edge(leaf_node, "End", 0)


    # get_node_applications

    def get_node_applications(self, node_id, attribute_name):

        # Return the nodes.

        return self.G.nodes[node_id][attribute_name]

        # Print out the node's attribute values give the node ID and attribute name.

      #  print ("Node ", node_id, "is named", self.G.nodes[node_id]["name"], "and contains attributes:", self.G.nodes[node_id][attribute_name])


    # print_node_applications

    def print_node_applications(self, node_id, attribute_name):

        # Print out the node's attribute values give the node ID and attribute name.

        print ("Node ", node_id, "is named", self.G.nodes[node_id]["name"], "and contains attributes:", self.G.nodes[node_id][attribute_name])


    def print_leaf_nodes(self, attribute_name):

        leaf_nodes = [node for node in self.G.nodes() if self.G.out_degree(node) == 0]

        print ("leaf nodes:", leaf_nodes)

        for leaf_node in leaf_nodes:
            self.print_node_applications(leaf_node, attribute_name)


    def get_shortest_path_nodes(self) -> []:

        source_node = "Start"
        dest_node = "End"

        return nx.astar_path(self.G, source_node, dest_node, heuristic=None, weight='manhattan_distance')


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

        if Global._debug: print ("BFS Edges:", graph_edges)

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


    # search_graph_by_multi_names

    def search_graph_by_multi_names(self, name_list, matched_nodes_list) -> []:

        if Global._debug: print ("Recursive search graph name_list", name_list)
        if Global._debug: print ("Recursive search graph matched_nodes_list", matched_nodes_list)

        # Check if there are still node names to be searched.
        if (len(name_list) > 0):

            # There is, get the last one in the list.

            node_to_match = name_list.pop()
            if Global._debug: print ("Recursive search graph matched_nodes_list node_to_match", node_to_match)

        else:

            # No more names to search, unwind the recursive calls by returning the matched_nodes_list.

            return matched_nodes_list

        # Do a breadth first search to get the list of nodes that match the node to match as
        # especially in the lower layers there can be multiple nodes.
        # (e.g., High_modernization)

        graph_edges = self.breadth_first_search('Start')

        matched_names_list = []

        # Iterate over the edges in the graph (u, v).

        for u, v in graph_edges:

            if Global._debug: print ("v = ", v)

            if (self.G.nodes[v].get("name") == node_to_match):

           #     if (v not in matched_nodes_list):
                matched_names_list.append(v)

        # matched_nodes_list = ['1', '1.2']

        if Global._debug: print ("Recursive search graph List of nodes that match", node_to_match, "are", matched_names_list)

        # If there are no matched names then the matched names list will be empty as the
        # matched names is a logical AND.

        if (len(matched_names_list) == 0):
        
            name_list.clear()

            return []

        # Iterate through the list of matched nodes to see if there is a path between it and
        # the current set.

        new_matched_nodes_list = []

        if (len(matched_nodes_list) == 0):

            new_matched_nodes_list = matched_names_list

        else:

            # Iterate through the matched names and matched nodes list to determine if there
            # is a path between the two nodes.  Account for direction (e.g., node 2.1.1 is further down
            # the tree than node 2.1).  Using a transitive relation: if there exists a path between
            # A -> B and there is a path between B -> C, then there is a path between A -> B -> C

            for source_node in matched_names_list:

                for target_node in matched_nodes_list:

                    if (source_node != target_node):

                        if (len(source_node) < len(target_node)):

                            path_exists = nx.has_path(self.G, source=source_node, target=target_node)
                            if Global._debug: print (f"Path exists between {source_node} and {target_node}: {path_exists}")
                            
                            if (path_exists):

                                new_matched_nodes_list.append(target_node)

                        else:

                            path_exists = nx.has_path(self.G, source=target_node, target=source_node)
                            if Global._debug: print (f"Path exists between {target_node} and {source_node}: {path_exists}")

                            if (path_exists):

                                new_matched_nodes_list.append(source_node)

        matched_nodes_list = new_matched_nodes_list


        if Global._debug: print ("Recursive search graph END matched_nodes_list", matched_nodes_list)

        return self.search_graph_by_multi_names(name_list, matched_nodes_list)


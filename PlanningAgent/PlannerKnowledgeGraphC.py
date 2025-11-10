# PlannerKnowledgeGraphC

# Import libraries.

import networkx as nx

class PlannerKnowledgeGraphC:

    # Constructor

    def __init__(self):
        self.G = nx.DiGraph()
        self.G.add_node("Start", node="Start", application="n/a")


    def add_node(self, node_name, application)

        # "ADD_NODE $application$ to TC-$technical_condition$"

        self.G.add_node(node_name, node=node_name, application=application)

    def add_edge(self, )

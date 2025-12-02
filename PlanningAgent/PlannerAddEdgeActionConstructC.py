# PlannerAddEdgeActionConstructC

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA
import Global


class PlannerAddEdgeActionConstructC(PlannerGraphActionConstructA):
   
    # Constructor

    def __init__(self):
        super().__init__()


    # invokeAction

    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph) -> {}:

        try:

            if Global._debug: print ("Add_Edge Action actionData:", actionData)
            if Global._debug: print ("Add_Edge Action dataDictionary:", dataDictionary)

            # Add dest to current weighted weight

            dest_node     = actionData[1] 
            current_node  = actionData[3] 
            weight        = actionData[5] 

            if Global._debug: print ("Add_Edge Action: an edge from", current_node, "to", dest_node, "weighted", weight, "will be created.")

            # Add the graph edge to the Planner Knowledge Graph.

            plannerKnowledgeGraph.add_edge(current_node, dest_node, weight)
      
            return dataDictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerAddEdgeActionConstructC Exception:", e)
            raise e


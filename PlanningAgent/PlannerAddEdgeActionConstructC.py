# PlannerAddNodeActionConstructC

from PlannerActionConstructA import PlannerActionConstructA
from PlannerGraphActionConstructA import PlannerGraphActionConstructA
import Global



class PlannerAddEdgeActionConstructC(PlannerGraphActionConstructA):
   
    def __init__(self):
        super().__init__()


    def invokeAction(self, dataDictionary, actionData, plannerKnowledgeGraph) -> {}:

        try:

            if Global._debug: print ("Add_Edge Action actionData:", actionData)
            if Global._debug: print ("Add_Edge Action dataDictionary:", dataDictionary)

            # Add dest to current weighted weight

            dest_node     = actionData[1] #.upper()  # .strip()
            current_node  = actionData[3]  #.delete('()').strip
            weight        = actionData[5]  #.delete('()').strip

            # TO_DO: if actionData[2] != 'to' or actionData[4] != 'weighted' then: Usage: ADD_EDGE <dest> to <current> weighted <weight>

            if Global._debug: print ("Add_Edge Action: an edge from", current_node, "to", dest_node, "weighted", weight, "will be created.")

            # Add the graph edge to the Planner Knowledge Graph.

            plannerKnowledgeGraph.add_edge(current_node, dest_node, weight)
      
            return dataDictionary

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("PlannerAddEdgeActionConstructC Exception:", e)
            raise e


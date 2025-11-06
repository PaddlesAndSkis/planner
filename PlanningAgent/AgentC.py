# AgentC

# Import Project classes.

from KnowledgeBaseC import KnowledgeBaseC
from PerceptionC import PerceptionC
from RulesEngineC import RulesEngineC

class AgentC:

    # Constructor

    def __init__(self):
        
        # Create the Agent modules.

        self.perception = PerceptionC()
        self.knowledge_base = KnowledgeBaseC()
        self.rules_engine = RulesEngineC()



    # add_to_data_dictionary

    def add_to_data_dictionary(self, data_dictionary):

        # Set the data dictionary in the Agent's Knowledge Base.

        self.knowledge_base.set_data_dictionary(data_dictionary)



    




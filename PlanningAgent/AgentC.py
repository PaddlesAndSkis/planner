# AgentC

# Import Project classes.

import Global

from KnowledgeBaseC import KnowledgeBaseC
from PerceptionC import PerceptionC
from RulesEngineC import RulesEngineC


class AgentC:

    # Constructor

    def __init__(self):
        
        pass


    # agent_goes_to_work

    def agent_goes_to_work(self, environment):

        # Set the environment in which the Agent will be operating.

        self.environment = environment

        # Build the Knowledge Base.

        kb = self.__build_knowledge_base()

        # Create the Perception module and invoke the plans.

        perception = PerceptionC(kb)
        perception.invoke_plans()


    # Private methods.

        
    # __build_knowledge_base

    def __build_knowledge_base(self) -> KnowledgeBaseC:

        # Create the Knowledge Base to get the rules and data dictionary.
        # The environment will have certain parameters to initialize the Knowledge Base.

        kb = KnowledgeBaseC(self.environment)

        # Create the Rules Engine with the Knowledge Base.

        rules_engine = RulesEngineC(kb)

        # Get the data set from the Environment.

        data_list = self.environment.load_data()

        # Get the initial data dictionary.

        data_dictionary = kb.get_data_dictionary()

        # Iterate over the data in the data list from the environment and
        # invoke the Rules Engine.

        for datum in data_list:

            # Update the data dictionary with the data from the data record.

            data_dictionary.update(datum)

            # Invoke the Rules Engine with the data dictionary.  Assign the data
            # dictionary that is returned for the next rule session.

            data_dictionary = rules_engine.invoke_rules(data_dictionary)

        
        # Update the Knowledge Base's data dictionary based on the last data dictionary.

        kb.set_data_dictionary(data_dictionary)

        # Set the Knowledge Graph in the Knowledge Base constructed from the Rules Engine.

        kb.set_knowledge_graph(rules_engine.get_knowledge_graph())

        # Return the Knowledge Base.

        return kb

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

        try:

            # Set the environment in which the Agent will be operating.

            self.environment = environment

            # Create the Perception module and gather the inputs from the environment.

            if Global._info: print ("Creating the Agent's Perception module")

            perception = PerceptionC(self.environment)
            plan_inputs = perception.gather_inputs_from_environment()

            # Create the Knowledge Base to get the rules and data dictionary.
            # The environment will have certain parameters to initialize the Knowledge Base.
            
            if Global._info: print ("Creating the Agent's Knowledge Base")

            kb = KnowledgeBaseC(self.environment)

            # Create the Rules Engine with the Knowledge Base.

            rules_engine = RulesEngineC(kb)

            # Build the Knowledge Graph.

            if Global._info: print ("Building the Agent's Knowledge Base's Knowledge Graph")

            kb = self.__build_knowledge_graph(kb, rules_engine)

            if Global._info: print ("Planning starts")

            # Invoke the plans retrieved from the environment.
            # Note that the Perception module can be called to get a Plan input.

            if Global._manual_drive:

                # Manual environment inputs.

                plan = ""

                while (plan.upper().strip() != Global._quit):
            
                    # Get the plan from the user.

                    plan_list = []
                    plan = perception.get_plan_from_user()

                    # Check to see if the user would like to quit.

                    if (plan.upper().strip() != Global._quit):

                        # The user has selected a plan.  Therefore, invoke it.

                        plan_list.append(plan)
                        self.__invoke_plans(plan_list, kb, rules_engine)

            else:
                
                # Auto environment inputs.

                self.__invoke_plans(plan_inputs, kb, rules_engine)


        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("AgentC Exception:", e) 
            raise e


    # Private methods.

        
    # __build_knowledge_graph

    def __build_knowledge_graph(self, kb, rules_engine) -> KnowledgeBaseC:

        try:

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

            # Once all the data records have been ingested, add the End node to the knowledge graph.

            (rules_engine.get_knowledge_graph()).add_end_node()

            # Update the Knowledge Base's data dictionary based on the last data dictionary.

            kb.set_data_dictionary(data_dictionary)

            # Set the Knowledge Graph in the Knowledge Base constructed from the Rules Engine.

            kb.set_knowledge_graph(rules_engine.get_knowledge_graph())

            # Return the Knowledge Base.

            return kb

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("AgentC exception:", e)
            raise e


    # __invoke_plans

    def __invoke_plans(self, plan_list, kb, rules_engine):

        try:

            # Get the initial data dictionary.

            data_dictionary = kb.get_data_dictionary()

            plan_kb = ({ "PLANNING" : "in_progress" })
            data_dictionary.update(plan_kb)

            # Iterate over the data in the data list from the environment and
            # invoke the Rules Engine.

            for plan in plan_list:

                # Set the plan name on the Knowledge Base.

                plan_kb = ({ "PLAN" : plan })

                # Update the data dictionary with the data from the data record.

                data_dictionary.update(plan_kb)

                # Invoke the Rules Engine with the data dictionary.  Assign the data
                # dictionary that is returned for the next rule session.

                data_dictionary = rules_engine.invoke_rules(data_dictionary)

        except Exception as e:

            # Catch, log and raise all exceptions.

            print ("AgentC Exception:", e)
            raise e
        





        # Get the Planner Knowledge Graph.

        #planner_knowledge_graph = self.kb.get_knowledge_graph()

        ## e.g.:
        ## self.perception.set_knowledge_graph(planner_knowledge_graph)

        #planner_knowledge_graph.print_node_applications("1.1.1.1", "application")
        #planner_knowledge_graph.print_leaf_nodes("application")
        #planner_knowledge_graph.add_end_node()
        
        #planner_knowledge_graph.print()
        #planner_knowledge_graph.print_shortest_path()
        #planner_knowledge_graph.print_longest_path()

        #print("If you know the name of the node, you can iterate through all the nodes and get the name:")
        #planner_knowledge_graph.search_graph_by_name("Low_business_value")
        #planner_knowledge_graph.search_graph_by_name("Low_technical_condition")

        #print("If you want to know which nodes have Low_business_value, Low_technical_condition, you must BFS:")
        #planner_knowledge_graph.search_graph_by_names('Low_business_value', 'Low_technical_condition')

        #print("If you want to get all the edges in a breadth first search:")
        #planner_knowledge_graph.breadth_first_search('Start')

        #print("Applications that should be Tolerated")
        #print("-------------------------------------")
        #print("The following applications have a low business value and a high technical condition, you must BFS:")
        #planner_knowledge_graph.search_graph_by_names('Low_business_value', 'Low_technical_condition')
        
        #print("If you want to know which nodes have high application risk, low modernization, you must BFS:")
        #planner_knowledge_graph.search_graph_by_names('High_application_risk', 'Low_modernization')

        #planner_knowledge_graph.print_node_applications("1", "application")
        #planner_knowledge_graph.print_node_applications("2", "application")


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

        #  Here are some charts:

        #  Here is the graph that was built to explore


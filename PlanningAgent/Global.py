# Global

# Global variables.

# Information display variables.

_debug = False
_info  = False

# Environment variables.

_manual_drive = True


# Plan variables.

_quit     = "quit"
_rebuild  = "rebuild"
_rehost   = "rehost"
_replace  = "replace"
_refactor = "refactor"
_retire   = "retire"
_sustain  = "sustain"
_tolerate = "tolerate"

_plan_list = [ _rebuild, _rehost, _replace, _refactor, _retire, _sustain, _tolerate, _quit ]

# Boolean Expression Parser variables.

_left_square_bracket = "["
_right_square_bracket = "]"
_condition_EOL = ";"
_and = "AND"
_or = "OR"

# Pointers to data that can be used outside the Agent.
    
_planner_knowledge_graph = None
_data_list = []
_rules = []


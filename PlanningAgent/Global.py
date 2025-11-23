# Global.py

# Global variables.

# Information display variables.

_debug = False
_info  = False

# Environment variables.

_manual_drive = True


# Plan variables.

_quit     = "QUIT"
_rebuild  = "rebuild"
_rehost   = "rehost"
_replace  = "replace"
_refactor = "refactor"
_retire   = "retire"
_sustain  = "sustain"

_plan_list = [ _rebuild, _rehost, _replace, _refactor, _retire, _sustain, _quit ]

# Boolean Expression Parser variables.

_left_square_bracket = "["
_right_square_bracket = "]"
_condition_EOL = ";"
_and = "AND"
_or = "OR"


#Rehost. Often referred to as lift and shift, this strategy is a cost-effective way to take advantage of a modern cloud infrastructure without modifying an application’s code.
#Replatform. Sometimes called lift, tinker, and shift, this strategy goes beyond rehosting, moving the application to a new runtime platform with minimal code changes.
#Refactor. This strategy involves changes to existing code without major changes to an application’s external behavior.
    # -> Low technical, high business, low app cost, low risk, low modernization
#Rebuild. Starting over is the right strategy when the cost of replatforming or refactoring outweighs the benefits. Rebuilding may be the only way to address legacy issues and incorporate new functionalities.
    # -> Low technical, high business, high app cost, high risk, low modernization
#Retire. This strategy means decommissioning or shutting down applications.
    # -> shortest path
#Retain. This strategy applies when your organization isn’t ready to modernize an application because of cost, dependencies, risks, or other factors.
    # -> high technical, low business, low app cost, low risk, low modernization
#Ideal
    # -> longest path
    # -> high technical, high business, low app cost, low risk, high modernization

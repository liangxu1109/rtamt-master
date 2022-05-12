from enum import Enum, unique

import rtamt.node.ltl.conjunction
from rtamt.node.ltl.always import Always
from rtamt.node.ltl.conjunction import Conjunction
from rtamt.node.ltl.disjunction import Disjunction



class Semantics(Enum):
    STANDARD = "standard"
    OUTPUT_ROBUSTNESS = "output-robustness"
    INPUT_VACUITY = "input-vacuity"
    INPUT_ROBUSTNESS = "input-robustness"
    OUTPUT_VACUITY = "output-vacuity"

    def __str__(self):
        return self.value

class Language(Enum):
    PYTHON = "python"
    CPP = "C++"
    def __str__(self):
        return self.value

class TimeInterpretation(Enum):
    DISCRETE = "discrete_time"
    DENSE = "dense-time"
    def __str__(self):
        return self.value

class RobustnessMetrics(Enum):
    AGM = "AGM"
    Standard = 'Traditional'
    def __str__(self):
        return self.value

class NodeType(Enum):
    And = Conjunction
    Or =  Disjunction
    def __str__(self):
        return self.value


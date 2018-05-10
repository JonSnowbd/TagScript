"""Filters is a collection of text modifiers
that have a specific purpose. For example having a Math Evaluation Filter
to take math blocks(m{10+10}) and evaluate them down to their result.
"""

from .math import MathEvaluationFilter
from .random import RandomFilter
from .variable import VariableFilter
from .optional import OptionalFilter
from .strf import STRFFilter
from .script import ScriptFilter
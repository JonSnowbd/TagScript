from ..interface import Sugar
import re

# FOR NOW DEPRECATED, need to decide on how sugars can be made opt-in
class AssignmentSugar(Sugar):
    def __init__(self):
        self.regex = re.compile(r"\<(.+)=(.+)\>")
    def replace(self, message) -> str:
        return message
    def repl_fn(self, match) -> str:
        return ""
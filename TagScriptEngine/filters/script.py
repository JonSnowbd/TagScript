import re, dukpy
from .safeinterp import SafeInterp

class ScriptFilter():

    def __init__(self):
        self.LOOKUP = re.compile(r"script{```[\w]*\n?([\S\s]+)\n?```\n?}")

    def Process(self, engine, text):
        script = self.LOOKUP.search(text).group(1)

        if(script == None):
            return text
        try:
            interp = SafeInterp()
            interp._funcs = {}

            self.SetupInterp(interp)

            return interp.evaljs(script)
        except dukpy.JSRuntimeError as e:
            return str(e)
        except AttributeError as e:
            return "Access is Denied on attribute acces or function call in script."

    def IsScript(self, text : str):
        return self.LOOKUP.search(text) is not None

    def SetupInterp(self, i : dukpy.JSInterpreter):
        i.evaljs("""
function Pick(ar){
    return ar[Math.floor(Math.random()*ar.length)];
}
        """)
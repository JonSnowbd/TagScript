import re, dukpy, discord
from .safeinterp import SafeInterp

class ScriptFilter():

    def __init__(self):
        self.LOOKUP = re.compile(r"script{```[\w]*\n?([\S\s]+)\n?```\n?}")
        self.EVAL = re.compile(r"[^\w]eval\(")
        self.Message : discord.Message = None

    def Process(self, engine, text, message : discord.Message = None):
        script = self.LOOKUP.search(text).group(1)
        if(self.EVAL.search(script) is not None):
            return "Eval is a blacklisted feature."
        if(script == None):
            return text
        try:
            interp = SafeInterp()
            interp._funcs = {}
            
            self.SetupInterp(interp)

            return interp.evaljs(script)
        except dukpy.JSRuntimeError as e:
            return "SCRIPT ERROR: ```"+str(e)+"```"
        except Exception as e:
            return str(e)

    def IsScript(self, text : str):
        """Returns a bool, True if the provided `text` of type string contains the script syntax"""
        return self.LOOKUP.search(text) is not None

    def SetupInterp(self, i : dukpy.JSInterpreter):
        i.evaljs("""
function Pick(ar){
    return ar[Math.floor(Math.random()*ar.length)];
}
        """)
        if self.Message is None:
            return
        mentionval = "false" if self.Message.mentions == [] or self.Message.mentions else "true"
        i.evaljs(f'var Mentions = {mentionval};')

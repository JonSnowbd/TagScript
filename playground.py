from TagScriptEngine import block, Interpreter, adapter
from appJar import gui

blocks = [
    block.MathBlock(),
    block.RandomBlock(),
    block.RangeBlock(),
    block.AnyBlock(),
    block.IfBlock(),
    block.AllBlock(),
    block.BreakBlock(),
    block.StrfBlock(),
    block.StopBlock(),
    block.AssignmentBlock(),
    block.FiftyFiftyBlock(),
    block.ShortCutRedirectBlock("message"),
    block.LooseVariableGetterBlock(),
	block.SubstringBlock()
]
x = Interpreter(blocks)

def press(button):
    o = x.process(app.getTextArea("input")).body
    app.clearTextArea("output")
    app.setTextArea("output", o)

app = gui("TSE Playground", "750x450")
app.setPadding([2,2])
app.setInPadding([2,2])
app.addTextArea("input", text="I see {rand:1,2,3,4} new items!", row=0, column=0)
app.addTextArea("output", text="Press process to continue", row=0, column=1)
app.addButton("process", press, row=1,column=0,colspan=2)
app.go()
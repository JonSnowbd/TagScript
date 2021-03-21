import TagScriptEngine as tse

blocks = [
    tse.MathBlock(),
    tse.RandomBlock(),
    tse.RangeBlock(),
    tse.AnyBlock(),
    tse.IfBlock(),
    tse.AllBlock(),
    tse.BreakBlock(),
    tse.StrfBlock(),
    tse.StopBlock(),
    tse.AssignmentBlock(),
    tse.FiftyFiftyBlock(),
    tse.ShortCutRedirectBlock("args"),
    tse.LooseVariableGetterBlock(),
    tse.SubstringBlock(),
    tse.EmbedBlock(),
    tse.ReplaceBlock(),
    tse.PythonBlock(),
    tse.URLEncodeBlock(),
    tse.RequireBlock(),
    tse.BlacklistBlock(),
    tse.CommandBlock(),
    tse.OverrideBlock(),
]
engine = tse.Interpreter(blocks)

msg = tse.escape_content("message provided :")
response = engine.process("{if({msg}==):provide a message|{msg}}", {"msg": tse.StringAdapter(msg)})

print(response)
print(response.body)

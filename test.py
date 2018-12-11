from TagScriptEngine import verb, engine, block

x = engine.Interpreter()
x.blocks.append(block.RandomBlock())

print(x.process("hello {random:{random:at home~in doors} people~animals}"))
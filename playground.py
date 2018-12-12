from TagScriptEngine import verb, engine, block

blocks = [
    block.RandomBlock(),
    block.RangeBlock(),
    block.FiftyFiftyBlock(),
    block.VariableGetterBlock()
]
x = engine.Interpreter(blocks)

print("====")
print("TagScriptEngine v2 Playground")
print("press Enter to submit a TSE string")
print("submit exit to leave. submit a blank to repeat previous.")
print("====")

user_input = input("> ")
previous = ""
while user_input != "exit":
    dummy_data = {
        "message": engine.StringAdapter("Hello, my name is PySnow")
    }
    result = None
    if user_input == "":
        result = x.process(previous, dummy_data)
    else:
        result = x.process(user_input, dummy_data)
        previous = user_input
    if result.error:
        print("ERROR ----")
        print(result.error_message)
    else:
        print(result.body)
    user_input = input("> ")
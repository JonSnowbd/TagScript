from ..TagScriptEngine import verb, engine, block
import unittest

def dummy_function():
    return 500

class TestVerbParsing(unittest.TestCase):
    def setUp(self):
        self.blocks = [
            block.StrictVariableGetterBlock()
        ]
        self.engine = engine.Interpreter(self.blocks)
    def tearDown(self):
        self.blocks = None
        self.engine = None

    def test_string_adapter(self):
        # Basic string adapter get
        data = {
            "test":engine.StringAdapter("Hello World")
        }
        result = self.engine.process("{test}", data).body
        self.assertEqual(result, "Hello World")

        # Slice
        result = self.engine.process("{test(1)}", data).body
        self.assertEqual(result, "Hello")

    def test_function_adapter(self):
        # Basic string adapter get
        data = {
            "fn": engine.FunctionAdapter(dummy_function)
        }
        result = self.engine.process("{fn}", data).body
        self.assertEqual(result, "500")


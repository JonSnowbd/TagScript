from ..TagScriptEngine import Verb, Interpreter, adapter, block
import unittest

def dummy_function():
    return 500

class TestVerbParsing(unittest.TestCase):
    def setUp(self):
        self.blocks = [
            block.StrictVariableGetterBlock()
        ]
        self.engine = Interpreter(self.blocks)
    def tearDown(self):
        self.blocks = None
        self.engine = None

    def test_string_adapter(self):
        # Basic string adapter get
        data = {
            "test":adapter.StringAdapter("Hello World, How are you")
        }
        result = self.engine.process("{test}", data).body
        self.assertEqual(result, "Hello World, How are you")

        # Slice
        result = self.engine.process("{test(1)}", data).body
        self.assertEqual(result, "Hello")

        # Plus
        result = self.engine.process("{test(3+)}", data).body
        self.assertEqual(result, "How are you")

        # up to
        result = self.engine.process("{test(+2)}", data).body
        self.assertEqual(result, "Hello World,")


    def test_function_adapter(self):
        # Basic string adapter get
        data = {
            "fn": adapter.FunctionAdapter(dummy_function)
        }
        result = self.engine.process("{fn}", data).body
        self.assertEqual(result, "500")


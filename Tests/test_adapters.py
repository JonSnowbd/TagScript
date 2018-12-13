from ..TagScriptEngine import verb, engine, block
import unittest

class TestVerbParsing(unittest.TestCase):
    def setUp(self):
        self.blocks = [
            block.VariableGetterBlock()
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


import unittest

from ..TagScriptEngine import Interpreter, Verb, adapter, block


class TestVerbParsing(unittest.TestCase):
    def test_basic(self):
        parsed = Verb("{hello:world}")
        self.assertTrue(type(parsed) is Verb)
        self.assertEqual(parsed.declaration, "hello")
        self.assertEqual(parsed.payload, "world")

        bare = Verb("{user}")
        self.assertEqual(bare.parameter, None)
        self.assertEqual(bare.payload, None)
        self.assertEqual(bare.declaration, "user")

        bare = Verb("{user(hello)}")
        self.assertEqual(bare.parameter, "hello")
        self.assertEqual(bare.payload, None)
        self.assertEqual(bare.declaration, "user")

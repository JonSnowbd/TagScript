from ..TagScriptEngine import verb, engine
import unittest
import asyncio

class TestVerbParsing(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()

    def test_basic(self):
        async def run():
            parsed = verb.parse("{hello:world}")
            self.assertTrue(type(parsed) is verb.Context)
            self.assertEqual(parsed.declaration, "hello")
            self.assertEqual(parsed.payload, "world")

            bare = verb.parse("{user}")
            self.assertEqual(bare.parameter, None)
            self.assertEqual(bare.payload, None)
            self.assertEqual(bare.declaration, "user")

            bare = verb.parse("{user(hello)}")
            self.assertEqual(bare.parameter, "hello")
            self.assertEqual(bare.payload, None)
            self.assertEqual(bare.declaration, "user")

        self.loop.run_until_complete(run())

    def test_interpretation(self):
        async def run():
            inter = engine.Interpreter()
            self.assertEqual(inter.get_deepest("{hello:{hello:world}{hello:world}}"), (7,19))
            self.assertEqual(inter.get_deepest("{hello:{hello:{hello:world}world}}"), (14,26))
            self.assertEqual(inter.replace_coordinates("{hello:{hello:world}}", (7,19), "world"), "{hello:world}")
        self.loop.run_until_complete(run())

    
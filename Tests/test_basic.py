from ..TagScriptEngine import verb
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
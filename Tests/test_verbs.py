from ..TagScriptEngine import verb, engine, block
import unittest
import asyncio

class TestVerbFunctionality(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        self.blocks = [
            block.MathBlock(),
            block.RandomBlock(),
            block.RangeBlock(),
            block.StrfBlock(),
            block.AssignmentBlock(),
            block.FiftyFiftyBlock(),
            block.VariableGetterBlock()
        ]
        self.engine = engine.Interpreter(self.blocks)
    def tearDown(self):
        self.blocks = None
        self.engine = None

    def seen_all(self, string, outcomes, tries=100):
        unique_outcomes = set(outcomes)
        seen_outcomes = set()
        for i in range(tries):
            outcome = self.engine.process(string).body
            seen_outcomes.add(outcome)

        result = unique_outcomes == seen_outcomes

        if result == False:
            print("Error from '"+string+"'")
            print("Seen:")
            for item in seen_outcomes:
                print("> "+str(item))
            print("Expected: ")
            for item in unique_outcomes:
                print(">> "+str(item))

        return result
        
    def test_random(self):
        # Test simple random
        test = "{random:Hello,Goodbye}"
        expect = ["Hello","Goodbye"]
        self.assertTrue(self.seen_all(test, expect))

        # Test that it wont crash with a false block
        test = "{random:{ahad},one,two}"
        expect = ["{ahad}","one","two"]
        self.assertTrue(self.seen_all(test, expect))

        # Test that inner blocks can use , to sep and outer use ~ without tripping
        # Also testing embedded random
        test = "{random:{random:1,2} cakes~No cakes}"
        expect = ["1 cakes", "2 cakes", "No cakes"]
        self.assertTrue(self.seen_all(test, expect))

        # Test random being able to use a var
        test = "{assign(li):1,2,3,4}{random:{li}}"
        expect = ["1","2","3","4"]
        self.assertTrue(self.seen_all(test, expect))

    def test_fifty(self):
        # Test simple 5050
        test = "Hi{5050: :)}"
        expect = ["Hi", "Hi :)"]
        self.assertTrue(self.seen_all(test, expect))

        # Test simple embedded 5050
        test = "Hi{5050: :){5050: :(}}"
        expect = ["Hi", "Hi :)", "Hi :) :("]
        self.assertTrue(self.seen_all(test, expect))

    def test_range(self):
        # Test simple 5050
        test = "{range:1-2} cows"
        expect = ["1 cows", "2 cows"]
        self.assertTrue(self.seen_all(test, expect))

    def test_misc(self):
        # Test using a variable to get a variable
        data = {
            "pointer": engine.StringAdapter("message"),
            "message": engine.StringAdapter("Hello")
        }
        test = "{{pointer}}"
        self.assertEqual(self.engine.process(test, data).body, "Hello")

        test = "\{{pointer}\}"
        self.assertEqual(self.engine.process(test, data).body, "\{message\}")
import TagScriptEngine
from unittest import TestCase

class test_optional_functionality(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======

    def test_basic_optional(self):
        had_nothing = False
        had_something = False

        for _ in range(300):
            message = self.engine.Process("?{Hello}")
            if message == "":
                had_nothing = True
            if message == "Hello":
                had_something = True

        self.assertTrue(had_nothing)
        self.assertTrue(had_something)

    def test_advanced_optional(self):
        had_nothing = False
        had_something = False

        for _ in range(300):
            message = self.engine.Process("#{x~?{Hello}~y}")
            if "Hello" not in message:
                had_nothing = True
            if "Hello" in message:
                had_something = True
            self.assertTrue("{" not in message)
            self.assertTrue("}" not in message)
            if had_nothing and had_something:
                break

        self.assertTrue(had_nothing)
        self.assertTrue(had_something)

    def test_nested_optional(self):
        had_nothing = False
        had_something = False

        for _ in range(700):
            message = self.engine.Process("#{x~?{Hello?{World}}~y}")
            if "World" not in message:
                had_nothing = True
            if "World" in message:
                had_something = True
            self.assertTrue("{" not in message)
            self.assertTrue("}" not in message)
            if had_nothing and had_something:
                break
            

        self.assertTrue(had_nothing)
        self.assertTrue(had_something)
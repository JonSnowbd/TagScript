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

        for x in range(300):
            message = self.engine.Process("?{Hello}")
            if message == "":
                had_nothing = True
            if message == "Hello":
                had_something = True

        self.assertTrue(had_nothing)
        self.assertTrue(had_something)
import TagScriptEngine
from unittest import TestCase

class test_strf_functionality(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======
    def test_basic_strf(self):
        """Lets uhh.. hope this wont cause a headache in 2019"""
        self.assertEqual(self.engine.Process("%y"), "2018")
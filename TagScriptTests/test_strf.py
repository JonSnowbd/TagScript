import time
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
        year = time.strftime("%Y")
        
        # backwards compativility
        if year == "2016":
            self.assertEqual(self.engine.Process("Hehe, it's strf{%Y}"), "Hehe, it's 2016")
        elif year == "2017": 
            self.assertEqual(self.engine.Process("Hehe, it's strf{%Y}"), "Hehe, it's 2017")
        elif year == "2018": 
            self.assertEqual(self.engine.Process("Hehe, it's strf{%Y}"), "Hehe, it's 2018")
        elif year == "2019": 
            self.assertEqual(self.engine.Process("Hehe, it's strf{%Y}"), "Hehe, it's 2019")
        else:
            # not yet supported
            self.assertTrue(False)

    def test_percentages(self):
        self.assertEqual(self.engine.Process("strf{%%}"), "%")

    def test_bad_formatting(self):
        self.assert_("<<strf error>> ValueError" in self.engine.Process("strf{%Y-%-m-%d}"))

    def test_complex_datetime(self):
        t = time.gmtime()
        curr_time = time.strftime("%Y-%m-%d", t)
        self.assertEqual(self.engine.Process("strf{%Y-%m-%d}"), curr_time)

    def test_locale(self):
        t = time.gmtime()
        curr_time = time.strftime("%c", t)
        self.assertEqual(self.engine.Process("strf{%c}"), curr_time)
import TagScriptEngine
from unittest import TestCase

class test_math_functionality(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======

    def test_weird_math(self):
        """Had problems with numbers like these."""
        self.engine.Add_Variable("unix", "1504891344.454338")
        self.engine.Process("m{$unix/10 - 1504891220}")

    def test_graceful_failure(self):
        message = self.engine.Process("m{lmao this should + $ ( **** not WOrk !$#}")
        self.assertEqual(message, "<<Math Failed>>")

    def test_negative_math(self):
        """Should handle negative math with some grace."""
        self.assertEqual(self.engine.Process("m{10-20}"), "-10")

    def test_basic_math(self):
        """Basic math, adds 10 and 10 to see if it returns 20."""
        self.assertEqual(self.engine.Process("m{10+10}"), "20", "adds 10 and 10")

    def test_basic_float_math(self):
        """Basic float math"""
        self.assertEqual(self.engine.Process("m{1/2}"), "0.5", "can divide into fractions")

    def test_advanced_math(self):
        """Advanced math, has nested math expressions that should add up to 40"""
        exp = "m{(10+10)+10+10}"
        self.assertEqual(self.engine.Process(exp), "40", "adds complex nested math")

    def test_basic_operators(self):
        """Basically a check for all the operators I'd expect to work"""
        exp = "m{100-9*2}"
        self.assertEqual(self.engine.Process(exp), "82")

        exp = "m{100+110}"
        self.assertEqual(self.engine.Process(exp), "210")

    def test_apply_order(self):
        """Should apply math in the correct order."""
        self.assertEqual(self.engine.Process("m{10*30^2}"), "9000", "applies correct order")

    def test_variable_math(self):
        """Should have no problem using a number provided through variables."""
        phrase = self.engine.Process("""!{x=100}\nm{$x+1}""")
        self.assertEqual(phrase, "101")

    def test_thirdparty_math(self):
        """First new math introduced to the operator block"""
        phrase = self.engine.Process("m{10%8}")
        self.assertEqual("2", str(phrase))

        phrase = self.engine.Process("m{log(50)}")
        self.assertEqual("1.6989700043360185", str(phrase))

        phrase = self.engine.Process("m{log2(50)}")
        self.assertEqual("5.643856189774724", str(phrase))
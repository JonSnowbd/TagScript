import TagScriptEngine
from unittest import TestCase

class test_random_functionality(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======

    def test_basic_random(self):
        phrase = self.engine.Process("Hello #{my dear friends~my dear friends}")
        self.assertEqual(phrase, "Hello my dear friends", "correctly parses randoms")
        self.assertNotIn("{", phrase)
        self.assertNotIn("}", phrase)
        self.assertNotIn("#", phrase)

    def test_basic_nested_random(self):
        for x in range(100):
            phrase = self.engine.Process("#{i bark #{loud~loud}~i bark loud}")
            self.assertEqual(phrase, "i bark loud")
            self.assertNotIn("{", phrase)
            self.assertNotIn("}", phrase)
            self.assertNotIn("#", phrase)

    def test_variable_compatibility(self):
        self.engine.Add_Variable("person", "carl")
        phrase = self.engine.Process("$person says hi to #{$person~carl}")
        self.assertEqual(phrase, "carl says hi to carl", "Is friendly with variables")

    def test_random_variable(self):
        phrase = self.engine.Process("""!{player1=#{Kintark~Yenni}}\n!{player2=Carl}\n$player1 says hi to $player2""")
        self.assertEqual(len(phrase.split(' ')), 5)
        self.assertNotIn("{", phrase)
        self.assertNotIn("}", phrase)
        self.assertNotIn("#", phrase)
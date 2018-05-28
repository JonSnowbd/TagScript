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
        for _ in range(100):
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

    def test_weighting(self):
        phrase = self.engine.Process("#{3|hello~goodbye} lads")
        self.assertNotIn("|", phrase)
    
    def test_longer_weightings(self):
        for i in range(200):
            phrase = self.engine.Process("has looted a #{45|960,30|965,18|970,8|975,3|980,985}")
            self.assertNotIn("|", phrase)

    def test_reusable_lists(self):
        for _ in range(200):
            phrase = self.engine.Process("#items{Coffee,Tea}\n$items $items").strip("\n")
            self.assertNotIn("#", phrase)
            self.assertNotIn("{", phrase)
            self.assertNotIn("}", phrase)
            self.assertNotIn("$", phrase)
            if(phrase == "Coffee Tea" or phrase == "Tea Coffee"):
                return
        self.assertTrue(False, "The reusable list is not being recalled for each iteration.")

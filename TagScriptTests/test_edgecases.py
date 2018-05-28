import TagScriptEngine
from unittest import TestCase

class test_edgecase_functionality(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======
    def test_edgecase_missing_var_in_math(self):

        self.engine.Add_Variable("1", "30")
        self.engine.Add_Variable("2", "2")
        #self.engine.Add_Variable("3", "0")
        trouble = self.engine.Process("m{($1+1+0$3=)*$2}")

        self.assertEqual("62", trouble)

    def test_edgecase_missing_var_in_math_substitute(self):

        self.engine.Add_Variable("1", "30")
        self.engine.Add_Variable("2", "2")
        #self.engine.Add_Variable("3", "0")
        trouble = self.engine.Process("m{($1+1+0$3=0)*$2}")

        self.assertEqual("62", trouble)

    def test_edgecase_variable_in_variable_assignment_isnt_replaced(self):
        self.engine.Add_Variable("user", "Carl#0001")

        trouble = self.engine.Process("!{f=#{hello $user~hello $user}}$f")

        self.assertEqual("hello Carl#0001", trouble)
    
    def test_edgecase_reusable_list_in_var_assignement(self):
        seen_yen = False
        seen_carl = False
        seen_py = False
        for _ in range(150):
            phrase = self.engine.Process("#user{carl,yenni,pysnow} !{player1=$user} $player1").strip(' ')
            if "pysnow" in phrase:
                seen_py = True
            if "carl" in phrase:
                seen_carl = True
            if "yenni" in phrase:
                seen_yen = True
        self.assertTrue(seen_carl and seen_py and seen_yen)
        
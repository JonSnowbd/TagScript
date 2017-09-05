import TagScriptEngine
from unittest import TestCase

class test_basic_functionality(TestCase):

    def test_basic_random(self):
        eng = TagScriptEngine.Engine()
        phrase = eng.Process("Hello #{my dear, friends~my humble compadres}")
        self.assertEquals(len(phrase.split(' ')), 4)
        self.assertTrue("{" not in phrase)
        self.assertTrue("}" not in phrase)
        self.assertTrue("#" not in phrase)

    def test_basic_nested_random(self):
        eng = TagScriptEngine.Engine()
        for x in range(100):
            phrase = eng.Process("#{i say #{hi~bye}~i bark loud}")
            #self.assertEquals(len(phrase.split(' ')), 3) TODO


    def test_basic_variables(self):
        eng = TagScriptEngine.Engine()
        phrase = eng.Process("""
!{player1=Kintark}
!{player2=Carl}
$player1 says hi to $player2""")
        self.assertEquals(len(phrase.split(' ')), 5)

    def test_outside_variables(self):
        eng = TagScriptEngine.Engine()
        eng.Add_Variable("me", "pysnow")
        phrase = eng.Process("$me $notme")
        self.assertEquals(phrase, "pysnow $notme")

    def test_mixing(self):
        eng = TagScriptEngine.Engine()
        eng.Add_Variable("person", "carl")
        phrase = eng.Process("$person says hi to #{$person~carl}")
        self.assertEquals(phrase, "carl says hi to carl")

    def test_random_variable(self):
        eng = TagScriptEngine.Engine()
        phrase = eng.Process("""!{player1=#{Kintark~Yenni}}
!{player2=Carl}
$player1 says hi to $player2""")
        print(phrase)
        self.assertEquals(len(phrase.split(' ')), 5)
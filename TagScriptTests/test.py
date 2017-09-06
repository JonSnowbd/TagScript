import TagScriptEngine
from unittest import TestCase

class test_basic_functionality(TestCase):

    def test_basic_math(self):
        gen = TagScriptEngine.Engine()
        phrase = gen.Process("m{10+10}")
        self.assertTrue(phrase == "20")

    def test_variable_math(self):
        gen = TagScriptEngine.Engine()
        phrase = gen.Process("""!{x=100}
m{$x+1}""")
        self.assertEquals(phrase, "101")

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
            self.assertEquals(len(phrase.split(' ')), 3)
            self.assertTrue("{" not in phrase)
            self.assertTrue("}" not in phrase)
            self.assertTrue("#" not in phrase)


    def test_basic_variables(self):
        eng = TagScriptEngine.Engine()
        phrase = eng.Process("""!{player1=Kintark}
!{player2=Carl}
$player1 says hi to $player2""")
        self.assertEquals(len(phrase.split(' ')), 5)


    def test_long_variables(self):
        eng = TagScriptEngine.Engine()
        phrase = eng.Process("!{ava=and this is a long variable with spaces!} say hi to $ava")
        self.assertEquals(phrase, "say hi to and this is a long variable with spaces!")

    def test_false_variables(self):
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
        self.assertEquals(len(phrase.split(' ')), 5)
        self.assertTrue("{" not in phrase)
        self.assertTrue("}" not in phrase)
        self.assertTrue("#" not in phrase)
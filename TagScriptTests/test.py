from TagScriptEngine import Engine
from unittest import TestCase

class test_basic_functionality(TestCase):

    def test_basic_random(self):
        x = Engine()
        self.assertEquals(len(x.Process("i can say #{hello~ding this works~fly high}").split(' ')), 4)

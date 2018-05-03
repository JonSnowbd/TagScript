import TagScriptEngine
from unittest import TestCase

class test_script_capability(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======
    def test_basic_script(self):
        scr = """script{```javascript
var i = ["hi", "bye"];
Pick(i)
```}"""
        seenhi = False
        seenbye = False
        
        for _ in range(300):
            if seenhi and seenbye:
                break
            p = self.engine.Process(scr)
            if p == "hi":
                seenhi = True
                continue
            elif p == "bye":
                seenbye = True
                continue

        self.assertTrue(seenhi and seenbye)

    def test_stuff(self):
        scr = """script{```javascript
var i = eval("var x = 80 * 80; x");
i
```}"""

        print("RETURNED: "+repr(self.engine.Process(scr)))

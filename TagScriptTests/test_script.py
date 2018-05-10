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

    def test_eval_cancel(self):
        scr = """script{```javascript
var i = eval("1*3");
i
```}"""
        self.assertIn("blacklisted", self.engine.Process(scr))

    def test_basic_injections(self):
        scr = """script{```javascript
var i;
if(Mentions){
    i = "There was a mention";
}else{
    i = "Didnt mention anything.";
}
i     
```}
"""
        #self.assertEqual("Didnt mention anything", self.engine.Process(scr))

# from ..TagScriptEngine import Verb, Interpreter, adapter, block, sugar
# import unittest

# class TestVerbFunctionality(unittest.TestCase):
#     def setUp(self):
#         self.blocks = [
#             block.BreakBlock(),
#             block.MathBlock(),
#             block.RandomBlock(),
#             block.RangeBlock(),
#             block.StrfBlock(),
#             block.AssignmentBlock(),
#             block.FiftyFiftyBlock(),
#             block.StrictVariableGetterBlock()
#         ]
#         self.sugars = [
#             sugar.AssignmentSugar()
#         ]
#         self.engine = Interpreter(self.blocks, self.sugars)
#     def tearDown(self):
#         self.blocks = None
#         self.engine = None

#     def testAssignmentSugar(self):
#         result = self.engine.prepare("<num=30>")
#         self.assertEqual(result, "{assign(num):30}")

# DEPRECATED FOR NOW
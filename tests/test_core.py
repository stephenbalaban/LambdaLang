import unittest
from core import *
class TestCore(unittest.TestCase):

    def test_identity(self):
        self.assertTrue(identity == identity(identity),
                "Losing my identity! Identity function failed!")

    def test_self_apply(self):
        self.assertTrue(identity == self_apply(identity),
                "Self application function failed to yield identity when passed identity!")

    def test_iszero(self):
        self.assertEquals(true, iszero(zero), 
                "zero != zero, the world explodes without a base case for the natural numbers group")
        self.assertEquals(false, iszero(succ(zero)),
                "zero == one, the world implodes because the successor function is broken in the natural numbers group")
        self.assertEquals(false, iszero(ten), "ten is confused with zero, what is going on?")


    def test_succ(self):
        pass

    def test_pred(self):
        self.assertEquals(one, pred(two), 
                "The predecessor function is breaking, you eat your grandfather")
        self.assertEquals(zero, pred(one),
                "The predecessor function is breaking from one -> zero, what?")



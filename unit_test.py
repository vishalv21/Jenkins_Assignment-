import unittest
from main import divide

class testdivide(unittest.TestCase):
  def testdivide1(self):
    self.assertEqual(divide (10, 5), 4)
    
if _name_ == '_main_':
  unittest.main()
import unittest
import action

class TestAction(unittest.TestCase):
  def test_suma(self):
    result = action.suma(30,5)
    self.assertEqual(result, 35)
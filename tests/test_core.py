import unittest
from termnet.core import endpoint
class Tests(unittest.TestCase):
 def test_port(self): self.assertEqual(endpoint('localhost',443).port,443)
 def test_invalid(self):
  with self.assertRaises(ValueError): endpoint('localhost',0)
if __name__=='__main__': unittest.main()

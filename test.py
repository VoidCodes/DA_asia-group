import unittest
from DA_asia_group import Statistics

class ProgramTest(unittest.TestCase):
    
    def testone(self):
         result = Statistics.getTopCountry("Japan")
         self.assertEqual(result, 3543798)
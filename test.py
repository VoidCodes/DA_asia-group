import unittest
from DA_asia_group import Statistics

class ProgramTest(unittest.TestCase):
    
    def testone(self):
        result = Statistics.generate_Top3()
        self.assertEquals(result)
import unittest
from timesheet import sum_timesheet

class TestTimeSheetSum(unittest.TestCase):
    def test_november_timesheet(self):
        self.assertEquals(
            79, sum_timesheet("timesheets/11_november.txt"),
            "timesheets/11_november.txt"
        )
        
    def test_december_timesheet(self):
        self.assertEquals(
            68, sum_timesheet("timesheets/12_december.txt"), 
            "timesheets/12_december.txt"
        )
        
    def test_january_timesheet(self):
        self.assertEquals(
             82.5, sum_timesheet("timesheets/01_january.txt"),
            "timesheets/01_january.txt"
        )
        
    def test_february_timesheet(self):
        self.assertEquals(
            73.5, sum_timesheet("timesheets/02_february.txt"),
            "timesheets/02_february.txt"
        )
        
    def test_march_timesheet(self):
        self.assertEquals(
            80, sum_timesheet("timesheets/03_march.txt"),
            "timesheets/03_march.txt"
        )
        
    def test_april_timesheet(self):
        self.assertEquals(
            34.25, sum_timesheet("timesheets/04_april.txt"), 
            "timesheets/04_april.txt"
        )
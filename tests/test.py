from unittest import TestCase
from generator.core import get_random_date

check_count = 100000

class HelloworldTestCase(TestCase):
    def test_format(self):
        for x in xrange(check_count):
            date = get_random_date()
            params = date.split('.')
            self.assertEqual(len(params),3,'Not valid date format need dd.mm.yyyy, {0}'.format(date))
            self.assertEqual(len(params[0]),2,'Not valid date format day must be 2 simbols, {0}'.format(date))
            self.assertEqual(len(params[1]),2,'Not valid date format moth must be 2 simbols, {0}'.format(date))
            self.assertEqual(len(params[2]),4,'Not valid date format year must be 4 simbols, {0}'.format(date))

    def test_day(self):
        for x in xrange(check_count):
            days_in_month = 31
            date = get_random_date()
            day = int(date.split('.')[0])
            month = int(date.split('.')[1])
            year = int(date.split('.')[2])
            if month!=2 and month%2 == 0 and month < 8:
                days_in_month = 30
            elif month!=2 and month%2 == 1 and month >= 8:
                 days_in_month = 30
            elif month==2 and year%400==0:
                days_in_month = 29
            elif month==2 and year%4 == 0 and year%100!=0:
                days_in_month = 29
            elif month==2:
                days_in_month = 28
            self.assertGreater(day,0,'Day "{0}" cant be  lower then 1, {1}'.format(day,date))
            self.assertLessEqual(day,days_in_month,'Day "{0}" cant be  greater then {1}, {2} '.format(day,days_in_month,date))

    def test_month(self):
        for x in xrange(check_count):
            date = get_random_date()
            month = int(date.split('.')[1])
            self.assertGreater(month,0,'Month "{0}" cant be  lower then 1, {1}'.format(month,date))
            self.assertLess(month,13,'Month "{0}" cant be  greater then 12, {1}'.format(month,date))


    


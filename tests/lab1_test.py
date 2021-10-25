import unittest
from PCPP1.Professional1.lab1 import TimeInterval


class TimeIntervalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.t1 = TimeInterval(hours=10, minutes=1, seconds=23)
        self.t2 = TimeInterval(hours=1, minutes=1, seconds=1)

    def test_should_print_HHMMSS(self):
        self.assertEqual(str(self.t1), '10:01:23')

    def test_should_return_hours_minutes_seconds(self):
        self.assertEqual(self.t1.gethours(), 10)
        self.assertEqual(self.t1.getminutes(), 1)
        self.assertEqual(self.t1.getseconds(), 23)

    def test_should_raise_type_error_onhour(self):
        with self.assertRaises(TypeError):
            t1 = TimeInterval(hours='test')

        with self.assertRaises(TypeError):
            t2 = TimeInterval(minutes='str')

        with self.assertRaises(TypeError):
            t3 = TimeInterval(seconds='str')

    def test_should_sum_two_times(self):
        t3 = self.t1 + self.t2
        self.assertEqual(t3.gethours(), 11)
        self.assertEqual(t3.getminutes(), 2)
        self.assertEqual(t3.getseconds(), 24)

    def test_should_not_overflow_on_seconds_sum(self):
        one_second = TimeInterval(seconds=1)
        t1 = TimeInterval(seconds=59)

        t2 = t1 + one_second
        self.assertEqual(t2.getminutes(), 1)
        self.assertEqual(t2.getseconds(), 0)

    def test_should_not_verflow_on_minutes_sum(self):
        one_minute = TimeInterval(minutes=1)
        t1 = TimeInterval(minutes=59)

        t2 = t1 + one_minute
        self.assertEqual(t2.gethours(), 1)
        self.assertEqual(t2.getminutes(), 0)

    def test_should_subtract(self): 
        t3 = self.t1 - self.t2

        self.assertEqual(t3.gethours(), 9)
        self.assertEqual(t3.getminutes(), 0)
        self.assertEqual(t3.getseconds(), 22)

    def test_should_multiply(self):
        t3 = self.t1 * 3
        self.assertEqual(t3.gethours(), 30)
        self.assertEqual(t3.getminutes(), 4)
        self.assertEqual(t3.getseconds(), 9)

    def test_should_not_be_negative(self):
        hour = TimeInterval(hours=1)
        t = hour - TimeInterval(minutes=1)

        self.assertEqual(t.gethours(), 0)
        self.assertEqual(t.getminutes(), 59)
        self.assertEqual(t.getseconds(), 0)

        t = t - TimeInterval(seconds=1)
        self.assertEqual(t.getminutes(), 58)
        self.assertEqual(t.getseconds(), 59)

    def test_subtract_integer(self):
        t = self.t1 - 2

        self.assertEqual(t.gethours(), 10)
        self.assertEqual(t.getminutes(), 1)
        self.assertEqual(t.getseconds(), 21)
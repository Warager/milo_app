from datetime import date
from django.test import TestCase
from milo_task.account.utils import get_eligible, get_bizzfuzz
import mock


class FakeDate(date):
    @classmethod
    def today(cls):
        return cls(2014, 10, 19)


class Utils_test(TestCase):
    @mock.patch("datetime.date", FakeDate)
    def test_get_eligible(self):
        date1 = date(1991, 12, 1)
        date2 = None
        date3 = date(2011, 3, 17)
        self.assertEqual(get_eligible(date1), 'allowed')
        self.assertEqual(get_eligible(date2), 'blocked')
        self.assertEqual(get_eligible(date3), 'blocked')

    def test_get_bizzfuzz(self):
        self.assertEqual(get_bizzfuzz(45), 'BizzFuzz')
        self.assertEqual(get_bizzfuzz(27), 'Bizz')
        self.assertEqual(get_bizzfuzz(40), 'Fuzz')
        self.assertEqual(get_bizzfuzz(22), 22)

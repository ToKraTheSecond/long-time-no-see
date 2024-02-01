import unittest

from long_time_no_see.statistics import summarize
from long_time_no_see.app import Encounter


class TestSummarizeMethod(unittest.TestCase):

    def test_summarize_empty_record(self):
        result = summarize([])
        self.assertEqual(result, {'total_meetings': 0, 'unique_people_met': []})

    def test_summarize_one_record(self):
        records = [Encounter(person='A')]
        result = summarize(records)
        self.assertEqual(result, {'total_meetings': 1, 'unique_people_met': ['A']})

    def test_summarize_four_records(self):
        records = [
            Encounter(person='A'),
            Encounter(person='B'),
            Encounter(person='C'),
            Encounter(person='D'),
        ]
        result = summarize(records)
        self.assertEqual(result['total_meetings'], 4)
        self.assertEqual(set(result['unique_people_met']), {'A', 'B', 'C', 'D'})

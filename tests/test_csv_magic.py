import unittest

from src.csv_magic import calculate_stats


class TestCalulateStats(unittest.TestCase):
    def test_calculate_stats_simple_case(self):
        data = [
            {
                "user_id": "1",
                "event_type": "GATE_IN",
                "event_time": "2023-02-01T08:00:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_OUT",
                "event_time": "2023-02-01T12:00:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_IN",
                "event_time": "2023-02-01T12:30:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_OUT",
                "event_time": "2023-02-01T17:00:00.000Z",
            },
        ]
        res1 = [("1", "8.5", "1", "8.5")]
        res2 = [("1", "8.5")]
        test_case = calculate_stats(data)
        self.assertEqual(test_case, (res1, res2))

    def test_calculate_stats_no_gate_in(self):
        data = [
            {
                "user_id": "1",
                "event_type": "GATE_OUT",
                "event_time": "2023-02-01T12:00:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_IN",
                "event_time": "2023-02-01T12:30:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_OUT",
                "event_time": "2023-02-01T17:00:00.000Z",
            },
        ]
        res1 = [("1", "16.5", "1", "16.5")]
        res2 = [("1", "16.5")]
        test_case = calculate_stats(data)
        self.assertEqual(test_case, (res1, res2))

    def test_calculate_stats_no_gate_out(self):
        data = [
            {
                "user_id": "1",
                "event_type": "GATE_IN",
                "event_time": "2023-02-01T08:00:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_OUT",
                "event_time": "2023-02-01T12:00:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_IN",
                "event_time": "2023-02-01T12:30:00.000Z",
            },
        ]
        res1 = [("1", "15.499722222222223", "1", "15.499722222222223")]
        res2 = [("1", "15.499722222222223")]
        test_case = calculate_stats(data)
        self.assertEqual(test_case, (res1, res2))

    def test_long_sessions(self):
        data = [
            {
                "user_id": "1",
                "event_type": "GATE_IN",
                "event_time": "2023-02-01T08:00:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_OUT",
                "event_time": "2023-02-01T12:00:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_IN",
                "event_time": "2023-02-01T16:30:00.000Z",
            },
            {
                "user_id": "1",
                "event_type": "GATE_OUT",
                "event_time": "2023-02-01T20:00:00.000Z",
            },
        ]
        res1 = [("1", "7.5", "1", "7.5")]
        res2 = [("1", "4.0")]
        test_case = calculate_stats(data)
        self.assertEqual(test_case, (res1, res2))

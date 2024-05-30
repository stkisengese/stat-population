import unittest
from math_skills import calculate_statistics

class TestMathSkills(unittest.TestCase):

    # Test calculating statistics with valid data.
    def test_calculate_stattistics_with_valid_data(self):
        data = [10.0, 20.0, 30.0, 40.0, 50.0]
        result = calculate_statistics(data)
        self.assertEqual(result, {
            'average': 30,
            'median': 30,
            'variance': 200,
            'std_dev': 14
        })

    # Test calculating statistics with empty data
    def test_calculate_statistics_with_empty_data(self):    
        result = calculate_statistics([])
        self.assertIsNone(result)

    # Test calculating statistics with single value
    def test_calculate_statistics_with_single_value(self):
        data = [36.9]
        result = calculate_statistics(data)
        self.assertEqual(result, {
            'average': 37,
            'median': 37,
            'variance': 0,
            'std_dev': 0
        })

if __name__ == "__main__":
    unittest.main(verbosity=2)
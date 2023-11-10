import unittest
from math_quiz import getRandomNumber, getRandomOperation, calculate

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = getRandomNumber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_getRandomOperation(self):
        # Test if the result is one of the expected operations
        operations = ['+', '-', '*']
        result = getRandomOperation()
        self.assertIn(result, operations)

    def test_calculate(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 3, '-', '10 - 3', 7),
                (4, 6, '*', '4 * 6', 24),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculate(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()

import unittest
from names import Survey


class TestCases(unittest.TestCase):

    def setUp(self):
        self.survey = Survey('What is your name?')
        self.responses = ['Narayana', 'Govinda', 'Krishna']

    def test_single(self):

        self.survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.survey.responses)

    def test_thrice(self):
        for x in self.responses:
            self.survey.store_response(x)
        for x in self.responses:
            self.assertIn(x, self.survey.responses)


if __name__ == '__main__':
    unittest.main()

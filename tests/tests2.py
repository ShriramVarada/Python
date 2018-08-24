import unittest
from names import Survey


class TestCases(unittest.TestCase):
    def test_single(self):
        survey = Survey('What is your name')
        survey.store_response('Shriram')
        self.assertIn('Shriram', survey.responses)

    def test_thrice(self):
        survey = Survey('What is your names')
        responses = ['sa', 'sdsd', 'ads']
        for x in responses:
            survey.store_response(x)
        for x in responses:
            self.assertIn(x, survey.responses)

unittest.main()
import unittest
import survey


class TestSurvey(unittest.TestCase):
    """ Tests for the AnonymousSurvey class """

    def setUp(self):
        """
           Create a survey and a set of responses for use in all test methods.
        """
        self.question = "q1"
        self.my_survey = survey.AnonymousSurvey(self.question)

    def test_store_single_response(self):
        """ Test that a single response is stored properly """
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()

import unittest
import survey


class TestSurvey(unittest.TestCase):
    """ Tests for the AnonymousSurvey class """

    def test_store_single_response(self):
        """ Test that a single response is stored properly """
        question = "q1"
        my_survey = survey.AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)


if __name__ == '__main__':
    unittest.main()

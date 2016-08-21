from django.test import TestCase


class AlgoAppTestCase(TestCase):
    """ Test Cases For Algo App"""
    def setUp(self):
        self.number = 6
        self.form_data = {'input_number': self.number}

    def test_algo_view_get(self):
        """Test for Algo View Get"""
        resp = self.client.get('/algo/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('<p>Enter The Number for which you want to get the Nth Number</p>' in resp.content)
        self.assertFalse('<p>Enter The Number for which you want to get the Nth Number HDHDHD</p>' in resp.content)

    def test_algo_view_post(self):
        """Test for Algo View Post"""
        expected_opt = 8
        resp = self.client.post('/algo/', self.form_data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('<h1>Result: <p>{}</p></h1>'.format(expected_opt) in resp.content)

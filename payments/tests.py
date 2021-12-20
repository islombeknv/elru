from django.test import TestCase
from django.test import Client
import hashlib


class TestClickUz(TestCase):
    client = Client()

    def test_authorization(self):
        data = {
            'click_trans_id': '14566027',
            'service_id': '1',
            'merchant_trans_id': '1',
            'merchant_prepare_id': '',
            'amount': '500',
            'action': '0',
            'error': '0',
            'error_note': 'Ok',
            'sign_time': '2020-05-04 01:45:28',
            'sign_string': '8350e2575f36fc310bfb29bb7c487bcd',
            'click_paydoc_id': '16853761'
        }
        response = self.client.post('/click/transaction/', data=data)
        self.assertEqual(response.data['error'], -1)
        self.assertEqual(response.data['error_note'], 'AUTHORIZATION_FAIL')

    def test(self):
        data = {
            'click_trans_id': '14566027',
            'service_id': '1',
            'merchant_trans_id': '1',
            'merchant_prepare_id': '',
            'amount': '500',
            'action': '0',
            'error': '0',
            'error_note': 'Ok',
            'sign_time': '2020-05-04 01:50:52',
            'sign_string': '7c4c1f53cbf8bb16c6b02a0083a75119',
            'click_paydoc_id': '16853761'
        }

        response = self.client.post('/click/transaction/', data=data)
        self.assertEqual(response.data['error'], '0')
        merchant_prepare_id = response.data['merchant_prepare_id']
        data['merchant_prepare_id'] = response.data['merchant_prepare_id']
        data['sign_string'] = self.generate_token(**data)

        response = self.client.post('/click/transaction/', data=data)
        self.assertEqual(response.data['error'], '0')

        data = {
            'click_trans_id': '14566027',
            'service_id': '1',
            'merchant_trans_id': '1',
            'merchant_prepare_id': '3',
            'amount': '1500',
            'action': '1',
            'error': '0',
            'error_note': 'Ok',
            'sign_time': '2020-05-04 02:15:07',
            'sign_string': 'a58eb470a1cb6e8795e7275312882fb8',
            'click_paydoc_id': '16853761'
        }
        response = self.client.post('/click/transaction/', data=data)
        self.assertEqual(response.data['error'], -2)

        data = {'click_trans_id': '14566027',
                'service_id': '1',
                'merchant_trans_id': '1',
                'merchant_prepare_id': merchant_prepare_id,
                'amount': '500',
                'action': '1',
                'error': '0',
                'error_note': 'Ok',
                'sign_time': '2020-05-04 02:17:51',
                'sign_string': '680f36aa3602e52c9350ff1261d0340b',
                'click_paydoc_id': '16853761'
                }
        data['sign_string'] = self.generate_token(**data)
        response = self.client.post('/click/transaction/', data=data)
        self.assertEqual(response.data['error'], '0')

    def generate_token(self, click_trans_id, amount, action, sign_time, merchant_trans_id,
                       merchant_prepare_id=None, *args, **kwargs):
        service_id = '1'
        secret_key = '1'
        text = f"{click_trans_id}{service_id}{secret_key}{merchant_trans_id}"
        if merchant_prepare_id != "" and merchant_prepare_id is not None:
            text += f"{merchant_prepare_id}"
        text += f"{amount}{action}{sign_time}"
        hash = hashlib.md5(text.encode('utf-8')).hexdigest()
        return hash

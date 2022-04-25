from unittest.mock import patch

from unittest import mock, TestCase

from requests import Session

from dhf_wrapper.client import PaymentClient
from dhf_wrapper.entities.payment import PaymentDTO


class TestPaymentClient(TestCase):
    @patch.object(Session, 'get')
    def test_positive_getting_payments(self, mock_get):
        payments = [
            {
                "data": [
                    {
                    "store": 60,
                    "amount": "2500000000",
                    "status": "Not_paid",
                    "comment": "Tips",
                    "type": 1,
                    "text": "Pay"
                    }
                ],
                "count": 0,
                "total": 0,
                "page": 0,
                "pageCount": 0
            }
        ]

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payments), json=lambda: payments)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient('http://example.com', token='xxxxx')

        response = payment_client.get_payments()

        self.assertEqual(response, payments)

    @patch.object(Session, 'get')
    def test_positive_getting_payment(self, mock_get):
        payment = {
            "data": [
                {
                "store": 60,
                "amount": "2500000000",
                "status": "Not_paid",
                "comment": "Tips",
                "type": 1,
                "text": "Pay"
                }
            ],
            "count": 0,
            "total": 0,
            "page": 0,
            "pageCount": 0
        }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payment), json=lambda: payment)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient('http://example.com', token='xxxxx')

        response = payment_client.get_payment(payment_id=1)

        self.assertEqual(response, payment)

    @patch.object(Session, 'post')
    def test_positive_create_payment(self, mock_post):
        payment_id = {
            "id": 1
        }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(post=mock.MagicMock(return_value=payment_id), json=lambda: payment_id)
        mock_post.return_value = mocked_session

        payment_client = PaymentClient('http://example.com', token='xxxxx')

        response = payment_client.create_payment(payment=PaymentDTO(
            amount=1234,
            comment="test"
        ))

        self.assertEqual(response, payment_id)

    @patch.object(Session, 'post')
    def test_negative_create_payment_without_params(self, mock_post):
        payment_id = {
            "id": 1
        }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(post=mock.MagicMock(return_value=payment_id), json=lambda: payment_id)
        mock_post.return_value = mocked_session

        payment_client = PaymentClient('http://example.com', token='xxxxx')

        with self.assertRaises(TypeError) as e:
            payment_client.create_payment()

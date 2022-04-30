from unittest.mock import patch

from unittest import mock, TestCase

from requests import Session

from dhf_wrapper.client import PaymentClient
from dhf_wrapper.entities.payment import PaymentDTO
from dhf_wrapper.exceptions import DHFUserUnauthorized, DHFBadRequest, DHFMethodNotFound


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
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payments),
                                                               json=lambda: payments)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        response = payment_client.get_payments()

        self.assertEqual(response, payments)

    @patch.object(Session, 'get')
    def test_negative_getting_payments_400_handling(self, mock_get):
        payments_400 = {"statusCode": 400,
                        "message": "Cannot GET /api/transactionsd",
                        "error": "Not Found"
                        }

        patch.object(Session, 'get')
        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payments_400),
                                                               json=lambda: payments_400)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(DHFBadRequest):
            payment_client.get_payments()

    @patch.object(Session, 'get')
    def test_negative_getting_payments_401_handling(self, mock_get):
        payments_401 = {"statusCode": 401,
                        "message": "Cannot GET /api/paymentss",
                        "error": "Not Found"
                        }

        patch.object(Session, 'get')
        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payments_401),
                                                               json=lambda: payments_401)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(DHFUserUnauthorized):
            payment_client.get_payments()

    @patch.object(Session, 'get')
    def test_negative_getting_payments_404_handling(self, mock_get):
        payments_404 = {"statusCode": 404,
                        "message": "Cannot GET /api/transactionsd",
                        "error": "Not Found"
                        }
        patch.object(Session, 'get')
        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payments_404),
                                                               json=lambda: payments_404)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(DHFMethodNotFound):
            payment_client.get_payments()

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
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payment),
                                                               json=lambda: payment)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        response = payment_client.get_payment(payment_id=1)

        self.assertEqual(response, payment)

    @patch.object(Session, 'get')
    def test_negative_getting_payment_400_handling(self, mock_get):
        payments_400 = {"statusCode": 400,
                        "message": "Cannot GET /api/transactionsd/1",
                        "error": "Not Found"
                        }
        patch.object(Session, 'get')
        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payments_400),
                                                               json=lambda: payments_400)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(DHFBadRequest):
            payment_client.get_payment(payment_id=1)

    @patch.object(Session, 'get')
    def test_negative_getting_payment_401_handling(self, mock_get):
        payments_401 = {"statusCode": 401,
                        "message": "Cannot GET /api/transactionsd",
                        "error": "Not Found"
                        }
        patch.object(Session, 'get')
        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payments_401),
                                                               json=lambda: payments_401)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(DHFUserUnauthorized):
            payment_client.get_payment(payment_id=1)

    @patch.object(Session, 'get')
    def test_negative_getting_payment_404_handling(self, mock_get):
        payments_404 = {"statusCode": 404,
                        "message": "Cannot GET /api/transactionsd",
                        "error": "Not Found"
                        }
        patch.object(Session, 'get')
        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=payments_404),
                                                               json=lambda: payments_404)
        mock_get.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(DHFMethodNotFound):
            payment_client.get_payment(payment_id=1)

    @patch.object(Session, 'post')
    def test_positive_create_payment(self, mock_post):
        payment_id = {
            "id": 1
        }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(post=mock.MagicMock(return_value=payment_id),
                                                               json=lambda: payment_id)
        mock_post.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

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
        mocked_session.__enter__.return_value = mock.MagicMock(post=mock.MagicMock(return_value=payment_id),
                                                               json=lambda: payment_id)
        mock_post.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(TypeError):
            payment_client.create_payment()

    @patch.object(Session, 'post')
    def test_negative_create_payment_400_handling(self, mock_post):
        payment_400 = {
            "statusCode": 400,
            "message": [
                "amount must not be less than 2500000000"
            ],
            "error": "Bad Request"
        }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(post=mock.MagicMock(return_value=payment_400),
                                                               json=lambda: payment_400)
        mock_post.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(DHFBadRequest):
            payment_client.create_payment(payment=PaymentDTO(
                amount=1234,
                comment="test"
            ))

    @patch.object(Session, 'post')
    def test_negative_create_payment_401_handling(self, mock_post):
        payment_401 = {"statusCode": 401,
                       "message": "Cannot GET /api/transactionsd",
                       "error": "Not Found"
                       }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(post=mock.MagicMock(return_value=payment_401),
                                                               json=lambda: payment_401)
        mock_post.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(DHFUserUnauthorized):
            payment_client.create_payment(payment=PaymentDTO(
                amount=1234,
                comment="test"
            ))

    @patch.object(Session, 'post')
    def test_negative_create_payment_404_handling(self, mock_post):
        payment_404 = {"statusCode": 404,
                       "message": "Cannot GET /api/transactionsd",
                       "error": "Not Found"
                       }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(post=mock.MagicMock(return_value=payment_404),
                                                               json=lambda: payment_404)
        mock_post.return_value = mocked_session

        payment_client = PaymentClient(base_url='http://example.com', token='xxxxx')

        with self.assertRaises(DHFMethodNotFound):
            payment_client.create_payment(payment=PaymentDTO(
                amount=1234,
                comment="test"
            ))

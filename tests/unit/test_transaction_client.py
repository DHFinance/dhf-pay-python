from unittest.mock import patch

from unittest import mock, TestCase

from requests import Session

from dhf_wrapper.client import TransactionClient
from dhf_wrapper.entities.transaction import TransactionParamsDTO
from dhf_wrapper.exceptions import DHFUserUnauthorized, DHFBadRequest, DHFMethodNotFound


class TestTransactionClient(TestCase):
    @patch.object(Session, 'get')
    def test_positive_getting_transactions(self, mock_get):
        transactions = [{
            "data": [
                {
                    "status": "processing",
                    "email": "kriruban1@gmail.com",
                    "updated": "2022-01-20 12:46:26.000",
                    "txHash": "16ae42729a88a4df9519a8e08807d68856070d93cf162898948b7de57e1a3368",
                    "payment": 2,
                    "sender": "01acdbbd933fd7aaedb7b1bd29c577027d86b5fafc422267a89fc386b7ebf420c9",
                    "amount": "2500000000"
                }
            ],
            "count": 0,
            "total": 0,
            "page": 0,
            "pageCount": 0
        }]

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=transactions),
                                                               json=lambda: transactions)
        mock_get.return_value = mocked_session

        transaction_client = TransactionClient(base_url='https://example.com', token='xxxxx')

        response = transaction_client.get_transactions(
            params=TransactionParamsDTO(limit=1)
        )

        self.assertEqual(response, transactions)

    @patch.object(Session, 'get')
    def test_negative_getting_transactions_connection_error(self, mock_get):
        mock_get.side_effect = ConnectionError()

        transaction_client = TransactionClient(base_url='https://example.com', token='xxxxx')

        with self.assertRaises(ConnectionError):
            transaction_client.get_transactions(
                params=TransactionParamsDTO(limit=1)
            )

    @patch.object(Session, 'get')
    def test_negative_getting_transactions_400_handling(self, mock_get):
        transactions_400 = {
            "statusCode": 400,
            "message": [
                "Some transaction getting error"
            ],
            "error": "Bad Request"
        }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=transactions_400),
                                                               json=lambda: transactions_400)
        mock_get.return_value = mocked_session
        transaction_client = TransactionClient(base_url='https://example.com', token='xxxxx')

        with self.assertRaises(DHFBadRequest):
            transaction_client.get_transactions(
                params=TransactionParamsDTO(limit=1)
            )

    @patch.object(Session, 'get')
    def test_negative_getting_transactions_401_handling(self, mock_get):
        transactions_401 = {
            "statusCode": 401,
            "message": "Cannot GET /api/transactions",
            "error": "Bad token"
        }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=transactions_401),
                                                               json=lambda: transactions_401)
        mock_get.return_value = mocked_session
        transaction_client = TransactionClient(base_url='https://example.com', token='xxxxx')

        with self.assertRaises(DHFUserUnauthorized):
            transaction_client.get_transactions(
                params=TransactionParamsDTO(limit=1)
            )

    @patch.object(Session, 'get')
    def test_negative_getting_transactions_404_handling(self, mock_get):
        transactions_404 = {
            "statusCode": 404,
            "message": "Cannot GET /api/transactionss",
            "error": "Not Found"
        }

        mocked_session = mock.MagicMock()
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=transactions_404),
                                                               json=lambda: transactions_404)
        mock_get.return_value = mocked_session
        transaction_client = TransactionClient(base_url='https://example.com', token='xxxxx')

        with self.assertRaises(DHFMethodNotFound):
            transaction_client.get_transactions(
                params=TransactionParamsDTO(limit=1)
            )

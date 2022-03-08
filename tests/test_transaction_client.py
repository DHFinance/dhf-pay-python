from unittest.mock import patch

from unittest import mock, TestCase

from requests import Session

from dhf_wrapper.client import TransactionClient
from dhf_wrapper.entities.transaction import TransactionParamsDTO


class TestTransactionClient(TestCase):
    @patch.object(Session, 'get')
    def test_getting_transactions_is_ok(self, mock_get):
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
        mocked_session.__enter__.return_value = mock.MagicMock(get=mock.MagicMock(return_value=transactions), json=lambda: transactions)
        mock_get.return_value = mocked_session

        transaction_client = TransactionClient('http://example.com', token='xxxxx')

        response = transaction_client.get_transactions(
            params=TransactionParamsDTO(limit=1)
        )

        self.assertEqual(response, transactions)

    @patch.object(Session, 'get')
    def test_getting_transactions_connection_error(self, mock_get):
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

        mock_get.side_effect = ConnectionError()

        transaction_client = TransactionClient('http://example.com', token='xxxxx')

        response = transaction_client.get_transactions(
            params=TransactionParamsDTO(limit=1)
        )

        self.assertEqual(response, transactions)

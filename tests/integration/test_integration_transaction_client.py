import os
from unittest import TestCase

from dhf_wrapper import TransactionClient
from dhf_wrapper.exceptions import DHFUserUnauthorized, DHFMethodNotFound


class TestIntegrationTransactionClient(TestCase):
    def setUp(self) -> None:
        self.token = os.getenv("TOKEN")
        self.url = os.getenv("API_BASE_URL")
        self.client = TransactionClient(base_url=self.url, token=self.token)

    def test_positive_get_transactions(self):
        response = self.client.get_transactions()
        self.assertIsInstance(response, list)

    def test_negative_get_transactions_no_token_handle_401(self):
        client = TransactionClient(base_url=self.url, token="")
        with self.assertRaises(DHFUserUnauthorized) as e:
            response = client.get_transactions()

    def test_negative_get_transactions_bad_url_handle_404(self):
        client = TransactionClient(base_url=self.url + "/api", token=self.token)
        with self.assertRaises(DHFMethodNotFound) as e:
            response = client.get_transactions()

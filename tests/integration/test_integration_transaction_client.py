import os
from unittest import TestCase

from dhf_wrapper import TransactionClient


class TestIntegrationTransactionClient(TestCase):
    def setUp(self) -> None:
        self.token = os.getenv("TOKEN")
        self.url = os.getenv("API_URL")
        self.client = TransactionClient(base_url=self.url, token=self.token)

    def test_positive_get_transactions(self):
        response = self.client.get_transactions()
        self.assertIsInstance(response, list)

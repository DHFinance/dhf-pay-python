import os
from unittest import TestCase

from dhf_wrapper import PaymentClient
from dhf_wrapper.entities.payment import PaymentDTO, PaymentIdDTO
from dhf_wrapper.entities.transaction import TransactionPaymentDTO
from dhf_wrapper.exceptions import DHFUserUnauthorized, DHFBadRequest, DHFMethodNotFound


class TestIntegrationPaymentClient(TestCase):
    def setUp(self) -> None:
        self.token = os.getenv("TOKEN")
        self.url = os.getenv("API_BASE_URL")
        self.client = PaymentClient(base_url=self.url, token=self.token)

    def test_positive_create_and_get_payment(self):
        payment = PaymentDTO(amount=2500000000, comment="Tips")
        response = self.client.create_payment(payment=payment)

        create_response_dto = PaymentIdDTO(**response)
        self.assertIsInstance(create_response_dto, PaymentIdDTO)

        response = self.client.get_payment(payment_id=create_response_dto.id)

        get_response_dto = TransactionPaymentDTO(**response)
        self.assertIsInstance(get_response_dto, TransactionPaymentDTO)
        self.assertEqual(get_response_dto.id, create_response_dto.id)

    def test_positive_get_payments_no_params(self):
        response = self.client.get_payments()

        self.assertIsInstance(response, list)

        for payment in response:
            payment_dto = TransactionPaymentDTO(**payment)
            self.assertIsInstance(payment_dto, TransactionPaymentDTO)

    def test_negative_get_payment_wrong_url_handle_404(self):
        client = PaymentClient(base_url=self.url + "/api", token="")
        with self.assertRaises(DHFMethodNotFound):
            client.get_payments()

    def test_negative_create_payment_bad_amount_handle_400(self):
        payment = PaymentDTO(amount=2, comment="Tips")
        with self.assertRaises(DHFBadRequest):
            self.client.create_payment(payment=payment)

    def test_negative_create_payment_no_token_handle_401(self):
        payment = PaymentDTO(amount=2500000000, comment="Tips")
        client = PaymentClient(base_url=self.url, token="")
        with self.assertRaises(DHFUserUnauthorized):
            client.create_payment(payment)

    def test_negative_create_payment_wrong_url_handle_404(self):
        payment = PaymentDTO(amount=2500000000, comment="Tips")
        client = PaymentClient(base_url=self.url + "/api", token=self.token)
        with self.assertRaises(DHFMethodNotFound):
            client.create_payment(payment)

    def test_negative_get_payments_no_token_handle_400(self):
        client = PaymentClient(base_url=self.url, token="")
        with self.assertRaises(DHFBadRequest):
            client.get_payments()

    def test_negative_get_payments_wrong_url_handle_404(self):
        client = PaymentClient(base_url=self.url + '/api', token="")
        with self.assertRaises(DHFMethodNotFound):
            client.get_payments()

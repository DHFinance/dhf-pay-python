import os
from unittest import TestCase

from dhf_wrapper import PaymentClient
from dhf_wrapper.entities.payment import PaymentDTO, PaymentIdDTO
from dhf_wrapper.entities.transaction import TransactionPaymentDTO


class TestIntegrationPaymentClient(TestCase):
    def setUp(self) -> None:
        self.token = os.getenv("TOKEN")
        self.url = os.getenv("API_BASE_URL")
        self.client = PaymentClient(base_url=self.url, token=self.token)

    def test_positive_create_and_get_payment(self):
        payment = PaymentDTO(amount=250000000000, comment="Tips")
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




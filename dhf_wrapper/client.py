from typing import Optional

from dhf_wrapper.base_client import ServiceClient

from dhf_wrapper.entities.params import ListParamsDTO
from dhf_wrapper.entities.payment import PaymentDTO
from dhf_wrapper.entities.transaction import TransactionParamsDTO


__all__ = ('PaymentClient', 'TransactionClient')


class PaymentClient(ServiceClient):
    PAYMENT_URL = "/api/payment"

    MAX_RETRIES = 3

    def create_payment(self, payment: PaymentDTO) -> dict:
        url = self.make_full_url(self.PAYMENT_URL)

        return self._make_request(request=self.session.post, url=url, json=payment.asdict())

    def get_payment(self, payment_id: int, params: ListParamsDTO = None) -> Optional[dict]:
        url = self.make_full_url(f"{self.PAYMENT_URL}/{payment_id}")

        return self._make_request(request=self.session.get, url=url, params=params.asdict())

    def get_payments(self, params: ListParamsDTO = None) -> dict:
        url = self.make_full_url(self.PAYMENT_URL)

        return self._make_request(request=self.session.get, url=url, params=params.asdict())


class TransactionClient(ServiceClient):
    TRANSACTION_URL = "/api/transaction"

    MAX_RETRIES = 3

    def get_transactions(self, params: TransactionParamsDTO) -> dict:
        url = self.make_full_url(self.TRANSACTION_URL)

        return self._make_request(request=self.session.get, url=url, params=params.asdict())

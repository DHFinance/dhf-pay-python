from typing import Optional

from dhf_wrapper.base_client import ServiceClient

from dhf_wrapper.entities.params import ListParamsDTO
from dhf_wrapper.entities.payment import PaymentDTO
from dhf_wrapper.entities.transaction import TransactionParamsDTO
from dhf_wrapper.exceptions import DHFMethodNotFound, DHFUserUnauthorized, DHFBadRequest, handle_exceptions

__all__ = ('PaymentClient', 'TransactionClient')


class PaymentClient(ServiceClient):
    PAYMENT_URL = "/api/payment"

    MAX_RETRIES = 3

    @handle_exceptions(exceptions=[DHFMethodNotFound, DHFUserUnauthorized, DHFBadRequest])
    def create_payment(self, payment: PaymentDTO) -> dict:
        """
        Class method to create a payment
        :param payment: PaymentDTO object
        :return: dict
        """
        url = self.make_full_url(self.PAYMENT_URL)

        return self._make_request(request=self.session.post, url=url, json=payment.asdict())

    @handle_exceptions(exceptions=[DHFMethodNotFound, DHFUserUnauthorized, DHFBadRequest])
    def get_payment(self, payment_id: int, params: ListParamsDTO = None) -> Optional[dict]:
        """
        Class method to get a payment by params
        :param payment_id: int
        :param params:  ListParamsDTO
        :return: Optional
        """
        url = self.make_full_url(f"{self.PAYMENT_URL}/{payment_id}")
        params = params.asdict() if params else None
        return self._make_request(request=self.session.get, url=url, params=params)

    @handle_exceptions(exceptions=[DHFMethodNotFound, DHFUserUnauthorized, DHFBadRequest])
    def get_payments(self, params: ListParamsDTO = None) -> dict:
        """
        Class method to get a payments list
        :param params:  ListParamsDTO
        :return: dict
        """
        url = self.make_full_url(self.PAYMENT_URL)
        params = params.asdict() if params else None
        return self._make_request(request=self.session.get, url=url, params=params)


class TransactionClient(ServiceClient):
    TRANSACTION_URL = "/api/transaction"

    MAX_RETRIES = 3

    @handle_exceptions(exceptions=[DHFMethodNotFound, DHFUserUnauthorized, DHFBadRequest])
    def get_transactions(self, params: TransactionParamsDTO = None) -> dict:
        """
        Class method to get a transactions list
        :param params:  ListParamsDTO
        :return: dict
        """
        url = self.make_full_url(self.TRANSACTION_URL)
        params = params.asdict() if params else None
        return self._make_request(request=self.session.get, url=url, params=params)

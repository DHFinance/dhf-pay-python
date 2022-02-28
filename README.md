# DHF-SDK

Python SDK to integrate with DHFinance in minutes.

## Installation

Local build:
```shell
python setup.py install
```

## Usage

```python
from dhf_wrapper.client import TransactionClient, PaymentClient
from dhf_wrapper.entities.transaction import TransactionParamsDTO
from dhf_wrapper.entities.payment import PaymentDTO

transaction_client = TransactionClient('http://example.com', token='xxxxx')

transactions = transaction_client.get_transactions(
    params=TransactionParamsDTO(limit=1)
)

payment_client = PaymentClient('http://example.com', token='xxxxx')

payments = payment_client.get_payments()
payment = payment_client.get_payment(payment_id=1)
new_payment = payment_client.create_payment(payment=PaymentDTO(
    store=2,
    amount=1234,
    status='paid',
    comment="test",
    type=1,
    text="test",
))
```

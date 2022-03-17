==================================
DHF-SDK
==================================

Python SDK to integrate with DHFinance in minutes.


Requirements
===============
Python 3.7

Installation
===============

Local build:

.. code-block::

    python setup.py install

From PyPi:

.. code-block::

    pip install dhf-sdk


Usage
===============
.. code-block::

    from dhf_wrapper.client import TransactionClient, PaymentClient
    from dhf_wrapper.entities.transaction import TransactionParamsDTO
    from dhf_wrapper.entities.payment import PaymentDTO

    transaction_client = TransactionClient('http://example.com', token='xxxxx')

    #Get transactions list
    transactions = transaction_client.get_transactions(
        params=TransactionParamsDTO(limit=1)
    )

    payment_client = PaymentClient('http://example.com', token='xxxxx')

    #Get payments list
    payments = payment_client.get_payments()

    #Get payments by id
    payment = payment_client.get_payment(payment_id=1)

    #Add new payment
    new_payment = payment_client.create_payment(payment=PaymentDTO(
        amount=1234,
        comment="test",
    ))

Run tests
===============

.. code-block::

    nosetests --verbosity=2 tests


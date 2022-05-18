==================================
DHF-SDK
==================================

Python SDK to integrate with DHFinance in minutes.

Getting Started
===============
1. **Sign up** - Before you begin, you need to sign up for your payment gateway account (https://pay.dhfi.online as example) and retrieve your store API token (add Store - APIKey Generate) and API_URL (https://pay.dhfi.online/api as example). 
2. **Requirements** – To run the SDK, your system will need to have Python >= 3.7.
3. **Install**

Local build:

.. code-block::

    python setup.py install --user

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
        amount=2500000000,
        comment="test",
    ))

Note: amount should be in motes, for exaple 1 cspr =  1000000000 in mots

Run tests
===============
**To run unit tests:**

.. code-block::

    nosetests --verbosity=2 tests/unit

**To run integration tests set up environment variables:**

::


    TOKEN - Store API key.
    API_BASE_URL - Base URL.

**And then call for tests:**

.. code-block::

    nosetests --verbosity=2 tests/integration

## Envorements

To set up your own environment replace  them in Dockerfile in lines 

``ENV TOKEN=BbhHiByZKYesWZeVQs00hiFCPOuqnHrDCtwh``

``ENV API_BASE_URL=https://pay.dhfi.online/``

## How to use
build ``make build``

enter to container ``make sh``

run tests 

``nosetests --verbosity=2 tests/unit``

``nosetests --verbosity=2 tests/integration``


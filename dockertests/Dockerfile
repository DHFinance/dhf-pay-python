FROM python:3.9
RUN pip install coverage nose nose-watch

WORKDIR /usr/src/app

RUN git clone https://github.com/DHFinance/dhf-pay-python.git .
RUN python setup.py install
ENV TOKEN=BbhHiByZKYesWZeVQs00hiFCPOuqnHrDCtwh
ENV API_BASE_URL=https://pay.dhfi.online/

#RUN export TOKEN=BbhHiByZKYesWZeVQs00hiFCPOuqnHrDCtwh
#RUN export API_BASE_URL=https://pay.dhfi.online/

#RUN pip install nose

#RUN nosetests --verbosity=2 tests/unit


#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]

from typing import Optional, Callable

import requests
from requests.auth import AuthBase
from requests.exceptions import RequestException

from dhf_wrapper.exceptions import HANDLED_ERRORS


class BearerAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'Bearer {self.token}'
        return r


class ServiceClient:
    DEFAULT_MAX_RETRIES = 0

    def __init__(
        self,
        base_url: str,
        token: Optional[str] = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.session = self._create_client_session()

    def _dispose(self):
        """
        Class method to close user session
        """
        self.session.close()

    def _create_client_session(self):
        """
        Class method to create client session
        """
        session = requests.Session()
        session.auth = self._get_http_auth()
        return session

    def _get_http_auth(self):
        """
        Class method to resolve http authentication
        """
        if self.token:
            return BearerAuth(self.token)

    def make_full_url(self, path: str) -> str:
        """
        Class method to make full url
        :param path: str
        :return: str
        """
        return f"{self.base_url}{path}"

    def _make_request(self, request: Callable, retries=DEFAULT_MAX_RETRIES, **kwargs) -> dict:
        """
        Class method to make request
        :param request: Callable
        :return: dict
        """
        try:
            with request(**kwargs) as resp:
                if resp.status_code not in HANDLED_ERRORS:
                    resp.raise_for_status()
                return resp.json()
        except RequestException as e:
            if retries > 0 and e.request.status >= 500:
                return self._make_request(request=request, retries=retries - 1, **kwargs)
            else:
                raise e

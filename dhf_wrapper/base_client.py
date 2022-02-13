from typing import Optional, Callable

import requests
from requests.auth import AuthBase
from requests.exceptions import RequestException


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
        self.session.close()

    def _create_client_session(self):
        session = requests.Session()
        session.auth = self._get_http_auth()
        return session

    def _get_http_auth(self):
        if self.token:
            return BearerAuth(self.token)

    def make_full_url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def _make_request(self, request: Callable, retries=DEFAULT_MAX_RETRIES, **kwargs) -> dict:
        try:
            with request(**kwargs) as resp:
                resp.raise_for_status()
                return resp.json()
        except RequestException as e:
            if retries > 0 and e.request.status >= 500:
                return self._make_request(request=request, retries=retries - 1, **kwargs)
            else:
                raise e

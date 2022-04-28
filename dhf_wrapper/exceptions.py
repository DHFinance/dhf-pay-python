from functools import wraps
from typing import List, Union, Type


HANDLED_ERRORS = (400, 401, 404)


class DHFBaseClientException(Exception):
    STATUS_CODE = 0


class DHFBadRequest(DHFBaseClientException):
    STATUS_CODE = 400


class DHFUserUnauthorized(DHFBaseClientException):
    STATUS_CODE = 401


class DHFMethodNotFound(DHFBaseClientException):
    STATUS_CODE = 404


def handle_exceptions(exceptions: List[Type[DHFBaseClientException]]):
    def deco(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                response: Union[dict, list] = func(*args, **kwargs)
                if isinstance(response, dict):
                    if response.get("statusCode", None):
                        err_code = response["statusCode"]
                        handled_errors = {exception.STATUS_CODE: exception for exception in exceptions}
                        err_message = f"Status code: {err_code}. " \
                                      f"Error: {response.get('error', None)}. " \
                                      f"Message: {response.get('message', None)}."
                        if err_code in handled_errors.keys():
                            raise handled_errors[err_code](err_message)
                        raise DHFBaseClientException(f"Unspecified error occured. {err_message}")
                return response
            except Exception as e:
                raise e
        return inner
    return deco

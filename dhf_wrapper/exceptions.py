from functools import wraps
from typing import List, Union, Type, Callable


HANDLED_ERRORS = (400, 401, 404)


class DHFBaseClientException(Exception):
    """
    Base Exception.
    """
    STATUS_CODE = 0


class DHFBadRequest(DHFBaseClientException):
    """
    Bad Request Exception, should be raised for all responses from API with status code 400.
    """
    STATUS_CODE = 400


class DHFUserUnauthorized(DHFBaseClientException):
    """
    User Unauthorized Exception, should be raised for all responses from API with status code 401.
    """
    STATUS_CODE = 401


class DHFMethodNotFound(DHFBaseClientException):
    """
    Method Not Found Exception, should be raised for all responses from API with status code 404.
    """
    STATUS_CODE = 404


def handle_exceptions(exceptions: List[Type[DHFBaseClientException]]) -> Callable:
    """
    Decorator for declaring handled exceptions.
    :param exceptions: List[Type[DHFBaseClientException]]
    :return: Callable
    """
    def deco(func) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs) -> Union[Union[dict, list], Union[DHFBaseClientException,
                                                                     DHFBadRequest,
                                                                     DHFMethodNotFound,
                                                                     DHFUserUnauthorized]]:
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

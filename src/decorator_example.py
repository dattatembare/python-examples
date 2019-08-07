import logging
from functools import wraps

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('start...')
        result = func(*args, **kwargs)
        logging.info('end...')
        return result

    return wrapper


@trace
def test_trace():
    logging.info('Executing method code..')


test_trace()

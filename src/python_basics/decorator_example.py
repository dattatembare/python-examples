"""
Decorator is a wraper function around original function, it extends the behaviour of original function
without modifying the original function's behaviour.
"""
import logging
from functools import wraps

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def trace(func):
    @wraps(func)  # wraps helps to keep original functions name as is
    def wrapper(*args, **kwargs):
        logging.info('start...')
        result = func(*args, **kwargs)
        logging.info('end...')
        return result

    return wrapper


# decorator with arguments
def timer(**deckwargs):
    def timer_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info('start...')
            logging.info(f'timer {deckwargs.get("on", False)}')
            result = func(*args, **kwargs)
            logging.info('end...')
            return result

        return wrapper

    return timer_dec


@trace
def test_trace():
    logging.info('Executing test_trace method code..')


test_trace()
# INFO:root:start...
# INFO:root:Executing test_trace method code..
# INFO:root:end...


@timer(on=True)
def test_timer():
    logging.info('Executing test_timer method code..')


test_timer()
# INFO:root:start...
# INFO:root:timer True
# INFO:root:Executing test_timer method code..
# INFO:root:end...

@timer()
def test_timer1():
    logging.info('Executing test_timer1 method code..')


test_timer1()
# INFO:root:start...
# INFO:root:timer False
# INFO:root:Executing test_timer1 method code..
# INFO:root:end...

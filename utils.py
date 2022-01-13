

def mylogging(logger=None):
    from datetime import datetime
    def wrapper(func):
        def inner(*args, **kwargs):
            start_at = datetime.now()
            fn_name = func.__name__
            msg = f"[{start_at}] start {fn_name} {args} {kwargs}"
            logger.debug(msg)
            obj = func(*args, **kwargs)
            finish_at = datetime.now()
            msg = f"[{finish_at}] finish {fn_name}({(finish_at-start_at).microseconds}ms)"
            logger.debug(msg)
            return obj
        return inner
    return wrapper


from logging import getLogger, DEBUG, StreamHandler, NullHandler

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)



@mylogging(logger)
def myfunc1(*args, **kwargs):
    print("Hello")

if __name__ == "__main__":
    myfunc1("ok", py="thon")

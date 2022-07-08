import time
from functools import wraps

def repeat(chances: int = 1, waiting_second: int = 3, *exceptions):
    def a(function):
        @wraps(function)
        def b(*args, **kwargs):
            for chance in range(chances, 0, -1):
                try:
                    return function(*args, **kwargs)
                except (exceptions):
                    print(f'[Chance : {chance}] "{function.__name__}" will be re-executed after {waiting_second} sec.', flush=True)
                    time.sleep(waiting_second)
            print(f'Exhaustion of all chances')
            raise TimeoutError
        return b
    return a
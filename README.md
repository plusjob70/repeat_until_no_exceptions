# repetition_until_no_exceptions
```python
from repeat import repeat_until_no_exceptions
```

# TEST

### Test code


```python
from random import randint

@repeat_until_no_exceptions(5, 2, IndexError)
def test_func(test_list: list):
    rdm_idx = randint(0, 10)
    print(f'{rdm_idx = }')
    return test_list[rdm_idx]
```

### Success in 5 chances


```python
test_func(['a', 'b', 'c', 'd'])
```

    rdm_idx = 4
    [Chance : 5] "test_func" will be re-executed after 2 sec.
    
    rdm_idx = 10
    [Chance : 4] "test_func" will be re-executed after 2 sec.
    
    rdm_idx = 3
    'd'



### Failure in 5 chances


```python
test_func(['a'])
```

    rdm_idx = 5
    [Chance : 5] "test_func" will be re-executed after 2 sec.
    
    rdm_idx = 2
    [Chance : 4] "test_func" will be re-executed after 2 sec.
    
    rdm_idx = 9
    [Chance : 3] "test_func" will be re-executed after 2 sec.
    
    rdm_idx = 9
    [Chance : 2] "test_func" will be re-executed after 2 sec.
    
    rdm_idx = 6
    [Chance : 1] "test_func" will be re-executed after 2 sec.
    
    Exhaustion of all chances



    ---------------------------------------------------------------------------

    TimeoutError          Traceback (most recent call last)

    File ~/repetition_until_no_exception/repeat.py:15, in repeat.<locals>.a.<locals>.b(*args, **kwargs)
         13         time.sleep(waiting_second)
         14 print(f'Exhaustion of all chances')
    ---> 15 raise TimeoutError


    TimeoutError: 


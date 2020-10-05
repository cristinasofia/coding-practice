## Exception Handling
```python
>>> def foo(denominator):
>>>     try:
>>>         return 42 / denominator
>>>     except ZeroDivisionError as e:
>>>         print('Error: Invalid argument: {}'.format(e))
>>> print(foo(0))
Error: Invalid argument: division by zero
```
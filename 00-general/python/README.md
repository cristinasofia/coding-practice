# Flow Control
## Pass
In Python programming, the pass statement is a null statement. The difference between a comment and a pass statement in Python is that while the interpreter ignores a comment entirely, pass is not ignored.

However, nothing happens when the pass is executed. It results in no operation (NOP).

# Functions
## Anonymous
In Python, an anonymous function is a function that is defined without a name. While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword. Hence, anonymous functions are also called lambda functions.

```python
>>> double = lambda x: x * 2
>>> double(5)
10

# example with filter()
>>> A = [1, 5, 4, 6, 8, 11, 3, 12]
>>> B = list(filter(lambda x: (x%2 == 0), A)
[4, 6, 8, 12]

# example with map()
>>> A = [1, 5, 4, 6, 8, 11, 3, 12]
>>> B = list(map(lambda x: x * 2, A)
[2, 10, 8, 12, 16, 22, 6, 24]
```

# Data Types

## Numbers
Int, float, complex

<table>
    <tr>
        <th>Number System</th>
        <th>Prefix</th>
    </tr>
    <tr>
        <td>Binary</td>
        <td>'0b' or '0B'</td>
    </tr>
    <tr>
        <td>Octal</td>
        <td>'0o' or '0O'</td>
    </tr>
    <tr>
        <td>Hexadecimal</td>
        <td>'0x' or '0X'</td>
    </tr>

</table>

### Decimal

```python
>>> (1.1 + 2.2) == 3.3
False

from decimal import Decimal as dec
>>> (dec(1.1) + dec(2.2)) == dec(3.3)
True
```

### Fraction
```python
from fraction import Fraction as frac
>>> frac(1.5)
3/2
>>> frac(1,3)
1/3

# do not create from float
>>> frac(1.1)
# garbage

# create from string
>>> frac('1.1')
11/10
```

### Math Operators
From highest to lowest precedence:
<table>
    <tr>
        <th>Operators</th>
        <th>Operations</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>**</td>
        <td>Exponent</td>
        <td>2 ** 3 = 8</td>
    </tr>
    <tr>
        <td>%</td>
        <td>Modulus</td>
        <td>22 % 8 = 6</td>
    </tr>
    <tr>
        <td>//</td>
        <td>Integer division (floor)</td>
        <td>22 // 8 = 2</td>
    </tr>
    <tr>
        <td>/</td>
        <td>Division</td>
        <td>22 / 8 = 2.75</td>
    </tr>
    <tr>
        <td>*</td>
        <td>Multiplication</td>
        <td>3 * 3 = 9</td>
    </tr>
    <tr>
        <td>-</td>
        <td>Substraction</td>
        <td>10 - 2 = 8</td>
    </tr>
    <tr>
        <td>+</td>
        <td>Addition</td>
        <td>3 + 4 = 7</td>
    </tr>

</table>

**Note:** bit operation modulo 2^t: for any s: s % (2^t) = s &(1<<t) - 1.

### Methods
```python
>>> float('inf') # MAX_INT
>>> float('-inf') # MIN_INT
```
For numeric types: max(x,y), min(x,y), abs(), math.ceil(), math.floor(), math.sqrt(), pow(x,y)
```python
>>> abs(-34.5)
34.5
>>> math.ceil(2.17)
3.0
>>> math.floor(3.14)
3.0
```
Type Convertions
```python
>>> str(42)
'42' # int to str
>>> int('42')
42 # str to int
```
Random
```python
>>> random.randrange(6)
0
>>> random.randint(1,6)
1
>>> random.random()
0.447166455429
>>> random.choice([3,99,4,67,81,2])
3
```

## Lists
### Methods
<div class="table-responsive">
	<table border="0">
		<tbody>
			<tr>
				<th><a href="/python-programming/methods/list">Python List Methods</a></th>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/append"><strong>append() -</strong></a> <a href="/python-programming/methods/list/append">Add an element to the end of the list</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/extend"><strong>extend()</strong></a> <a href="/python-programming/methods/list/extend">-</a> <a href="/python-programming/methods/list/extend">Add all elements of a list to the another list</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/insert"><strong>insert()</strong></a> <a href="/python-programming/methods/list/insert">-</a> <a href="/python-programming/methods/list/insert">Insert an item at the defined index</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/remove"><strong>remove()</strong></a> <a href="/python-programming/methods/list/remove">-</a> <a href="/python-programming/methods/list/remove">Removes an item from the list</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/pop"><strong>pop()</strong></a> <a href="/python-programming/methods/list/pop">-</a> <a href="/python-programming/methods/list/pop">Removes and returns an element at the given index</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/clear"><strong>clear()</strong></a> <a href="/python-programming/methods/list/clear">- Removes all items from the list</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/index"><strong>index()</strong></a> <a href="/python-programming/methods/list/index">- Returns the index of the first matched item</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/count"><strong>count()</strong></a> <a href="/python-programming/methods/list/count">- Returns the count of the number of items passed as an argument</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/sort"><strong>sort()</strong></a> <a href="/python-programming/methods/list/sort">- Sort items in a list in ascending order</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/reverse"><strong>reverse()</strong></a> <a href="/python-programming/methods/list/reverse">- Reverse the order of items in the list</a></td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/list/copy"><strong>copy()</strong></a> <a href="/python-programming/methods/list/copy">- R</a><a href="/python-programming/methods/list/copy">eturns a shallow copy of the list</a></td>
			</tr>
		</tbody>
	</table>
</div>

## Tuples
```python
>>> my_tuple = ('a', 'p', 'p', 'l', 'e',)

>>> my_tuple.count('p')
2
>>> my_tuple.index('l')
3
```
### Tuples vs Lists
- Tuples are used for heterogenuous data types, and lists for homogenuous data types
- Tuples are immutable (slight performance boost)
- Tuples can be used as keys in a dictionary
- Tuples guarantee write-protected data

# Sets
```python
>>> A = {1, 2, 3, 4, 5}
>>> B = {4, 5, 6, 7, 8}

# union
>>> A | B
{1, 2, 3, 4, 5, 6, 7, 8}

# intersection
>>> A & B
{4, 5}

# difference
>>> A - B
{1, 2, 3}

# symmetric difference
>>> A ^ B
{1, 2, 3, 6, 7, 8}
```

discard() - Removes an element from the set if it is a member. (Do nothing if the element is not in set)
pop() - Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove() - Removes an element from the set. If the element is not a member, raises a KeyError

<div class="table-responsive">
	<table border="0">
		<tbody>
			<tr>
				<th>Function</th>
				<th>Description</th>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/all">all()</a></td>
				<td>Returns <code>True</code> if all elements of the set are true (or if the set is empty).</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/any">any()</a></td>
				<td>Returns <code>True</code> if any element of the set is true. If the set is empty, returns <code>False</code>.</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/enumerate">enumerate()</a></td>
				<td>Returns an enumerate object. It contains the index and value for all the items of the set as a pair.</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/len">len()</a></td>
				<td>Returns the length (the number of items) in the set.</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/max">max()</a></td>
				<td>Returns the largest item in the set.</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/min">min()</a></td>
				<td>Returns the smallest item in the set.</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/sorted">sorted()</a></td>
				<td>Returns a new sorted list from elements in the set(does not sort the set itself).</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/sum">sum()</a></td>
				<td>Returns the sum of all elements in the set.</td>
			</tr>
		</tbody>
	</table>
</div>

# Dictionary

get(key[,d]) - Returns the value of the key. If the key does not exist, returns d (defaults to None).
items() - Return a new object of the dictionary's items in (key, value) format.
keys() - Returns a new object of the dictionary's keys.
pop(key[,d]) - Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.
popitem() - Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
values() - Returns a new object of the dictionary's values

<div class="table-responsive">
	<table border="0">
		<tbody>
			<tr>
				<th>Function</th>
				<th>Description</th>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/all">all()</a></td>
				<td>Return <code>True</code> if all keys of the dictionary are True (or if the dictionary is empty).</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/any">any()</a></td>
				<td>Return <code>True</code> if any key of the dictionary is true. If the dictionary is empty, return <code>False</code>.</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/len">len()</a></td>
				<td>Return the length (the number of items) in the dictionary.</td>
			</tr>
			<tr>
				<td>cmp()</td>
				<td>Compares items of two dictionaries. (Not available in Python 3)</td>
			</tr>
			<tr>
				<td><a href="/python-programming/methods/built-in/sorted">sorted()</a></td>
				<td>Return a new sorted list of keys in the dictionary.</td>
			</tr>
		</tbody>
	</table>
</div>

# Files

## Open
```python
>>> f = open("test.txt")
```
<table>
    <tr>
        <th>Mode</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>r</td>
        <td>Opens file to read.</td>
    </tr>
    <tr>
        <td>w</td>
        <td>Opens file to write.</td>
    </tr>
    <tr>
        <td>+</td>
        <td>Opens a file for updating (reading and writing)</td>
    </tr>
</table>

## Close
```python
>>> f.close()

>>> try: 
>>>     f = open("test.txt", encoding = 'utf-8')
>>> finally:
>>>     f.close()
```

## Write
```python
>>> with open("test.txt", 'w', encoding = 'utf-8') as f:
>>> f.write("My first file\n")
```

## Read
```python
>>> f = open("test.txt", encoding = 'utf-8')
>>> f.read(3)
'My '
>>> f.read(3)
'fir'
>>> f.read()
'st file\n'

>>> f.tell()    # get the current file position
13

>>> f.seek(0)   # bring file cursor to initial position
0

>>> f.readline()
'My first file\n'
```

## Exception
### Basic
```python
>>> def foo(denominator):
>>>     try:
>>>         return 42 / denominator
>>>     except ZeroDivisionError as e:
>>>         print('Error: Invalid argument: {}'.format(e))
>>> print(foo(0))
Error: Invalid argument: division by zero
```
### Final code in exception handling
```python
>>> def foo(denominator):
>>>     try:
>>>         return 42 / denominator
>>>     except ZeroDivisionError as e:
>>>         print('Error: Invalid argument: {}'.format(e))
>>>     finally:
>>>         print("-- done --")
>>> print(foo(0))
Error: Invalid argument: division by zero
-- done --
```

# Object and Class

# Advanced Topics

# Data and Time
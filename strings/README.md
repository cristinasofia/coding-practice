# Python
Strings are immutable in Python. This means that once a string has been defined, it can’t be changed.

There are no mutating methods for strings. This is unlike data types like lists, which can be modified once they are created.

## Manipulating Strings
### Escape Characters
<table>
    <tr>
        <th>Escape Character</th>
        <th>Prints as</th>
    </tr>
    <tr>
        <td>\'</td>
        <td>Single quote</td>
    </tr>
    <tr>
        <td>\"</td>
        <td>Double quote</td>
    </tr>
    <tr>
        <td>\t</td>
        <td>Tab</td>
    </tr>
    <tr>
        <td>\n</td>
        <td>Newline (line break)</td>
    </tr>
    <tr>
        <td>\\</td>
        <td>Backslash</td>
    </tr>
</table>

```python
H   e   l   l   o       W   o   r   l   d   !
0   1   2   3   4   5   6   7   8   9   10  11
```

### Indexing
```python
>>> x = 'Hello world!'
>>> x[0]
'H'
>>> x[-1]
'!'
```
### Slicing
```python
>>> x[0:5]
'Hello'
>>> x[:5]
'Hello'
>>> x[3:7]
'lo W'
>>> x[-3:]
'ld!'
>>> x[::-1]
'!dlroW olleH'
```
### String Methods
upper() and lower()
```python
>>> x.upper()
'HELLO WORLD!'
>>> x.lower()
'hello world!'
```
isupper() and islower()
```python
>>> x[6].isupper() # 'W'
True
>>> x[6:].isupper() # 'World!'
False
>>> x[7:].islower() # 'orld!'
True
```
isalpha(), isalnum(), isdecimal(), isdigit(), isspace(), istitle()
```python
>>> x.isalpha()

>>> x.isalnum()

>>> x.isdecimal()

>>> x.isspace()

>>> x.istitle()

```
capitalize()
```python
>>> y = 'i love cookies'
>>> y.capitalize()
'I love cookies'
```
join()
```python
>>> A = ['Hello', 'world']
>>> B = [1, 2, 3]
# convert list to string:
>>> ' '.join(A)
'Hello World'
# use map() to convert each item in the list to a string, and then join them:
>>> ' '.join(map(str,B))
1 2 3
```
startswith() and endswith()
```python
>>> x.startswith('Hello')
True
>>> x.endswith('z')
False
```
split()
```python
>>> txt1 = 'Silicon Valley'
>>> txt1.split()
['Silicon', 'Valley']
>>> txt1.split('i')
['S', 'l', 'con Valley']
```
strip()
```python
>>> txt1 = '  apples and oranges  '
>>> txt1.strip()
'apples and oranges'
>>> txt2 = '..+..apples and oranges..-..'
>>> txt2.strip('.')
'+..apples and oranges..-'
>>> txt2.strip('.+')
'apples and oranges..-'
>>> txt2.strip('.+-')
'apples and oranges'
```
replace()
```python
>>> x = 'strawberry'
>>> x.replace('r','4')
'st4awbe44y'
```
title()
```python
>>> x = 'new york'
>>> x.title()
'New York'
```

### Regular Expressions
1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual matched text.
All the regex functions in Python are in the re module:
```python
>>> import re
```
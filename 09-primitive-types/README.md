# Python
## Comparison
<table>
    <tr>
        <th>Operator</th>
        <th>Meaning</th>
        <th>Boolean Equivalent</th>
    </tr>
    <tr>
        <td>==</td>
        <td>Equal to</td>
        <td>is</td>
    </tr>
    <tr>
        <td>!=</td>
        <td>Not equal to</td>
        <td>is not</td>
    </tr>
    <tr>
        <td><</td>
        <td>Less than</td>
        <td></td>
    </tr>
    <tr>
        <td>></td>
        <td>Greater than</td>
        <td></td>
    </tr>
    <tr>
        <td><=</td>
        <td>Less than or equal to</td>
        <td></td>
    </tr>
    <tr>
        <td>>=</td>
        <td>Greater than or equal to</td>
        <td></td>
    </tr>
</table>

## Boolean Operators
<table>
    <tr>
        <th>A</th>
        <th>B</th>
        <th>A and B</th>
        <th>A or B</th>
        <th>not A</th>
    </tr>
    <tr>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
    </tr>
</table>

## Bits
```python
1   0   1   0
3   2   1   0
```
Test kth bit is set
```python
def get_bit(x, k):
    return (x & (1 << k)) != 0

>>> get_bit(10, 2)
# 1   0   1   0
# 3   2   1   0
False
```
Set kth bit
```python
def set_bit(x, k):
    return x | (1 << k)

>>> set_bit(10, 0)
# 1   0   1   1
# 3   2   1   0
11
```
Turn off kth bit
```python
def clear_bit(x, k):
    return x & ~(1 << k)

>>> clear_bit(10, 1)
# 1   0   0   0
# 3   2   1   0
8
```
Toggle the kth bit
```python
def flip_bit(x, k):
    return x ^ (1 << k)

>>> flip_bit(10, 2)
# 1   1   0   0
# 3   2   1   0
14
```

## Useful Methods
Check if a number is a power of 2
```python
def is_power_of_2(x):
    return x & x - 1 == 0
```
Counting number of 1 bits
```python
# 191 https://leetcode.com/problems/number-of-1-bits/
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits
```
Parity: If number is even or odd (by number of counting bits)
```python
def parity(x):
    res = 0
    while x:
        res ^= x & 1
        x >>= 1
    return res
```

### Corner cases
- Be aware and check for overflow/underflow
- Negative numbers
# Object Oriented
Python is a multi-paradigm programming language. It supports different programming approaches.

One of the popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

An object has two characteristics:
1. attributes
2. behavior (methods)

## Class
A class is a blueprint for the object. From class, we construct instances. An instance is a specific object created from a particular class.

## Object
An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

## Attributes
- A class attribute is a Python variable that belongs to a class rather than a particular object. 
  - It is shared between all the objects of this class.
  - Defined outside the constructor function.
- An instance attribute is a Python variable belonging to one, and only one, object. 
  - This variable is only accessible in the scope of this object.
  - Defined inside the constructor function.

```python
class Parrot:
   # class attribute
   species = "bird"
   count = 0

   # instance attribute
   def __init__(self, name, age):
      self.name = name
      self.age = age
      Parrot.count += 1

>>> blue = Parrot("Blu", 10)
>>> woo = Parrot("Woo", 15)

# access instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

# access class attribute
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))
print("There are {} parrot(s)".format(woo.__class__.count))
```

# Encapsulation
- Private attributes: underscore as the prefix i.e single _ or double __.

# Inheritance

Without inheritance:
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

>>> square = Square(4)
>>> square.area()
16
>>> rectangle = Rectangle(2,4)
>>> rectangle.area()
8
```

With inheritance:
```python
class Square(Rectangle):   # Square class inherits from Rectangle
    def __init__(self, length):
        super().__init__(length, length)  # call Rectangle constructor

>>> square = Square(4)
>>> square.area()
16
```

More applications of super():
```python
class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

>>> cube = Cube(3)
>>> cube.surface_area()
54
>>> cube.volume()
27
```

## Multiple Inheritance
A class can be derived from more than one base class in Python.
```python
# The MultiDerived class is derived from Base1 and Base2 classes.
class Base1:
    pass       # features of Base1

class Base2:
    pass       # features of Base2

class MultiDerived(Base1, Base2):
    pass       # features of Base1, Base2, and MultiDerived
```

## Multilevel Inheritance
Features of the base class and the derived class are inherited into the new derived class.
```python
# The Derived1 class is derived from the Base class, and the Derived2 class is derived from the Derived1 class.
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
```

# Polymorphism
When two Python classes offer the same set of methods with different implementations, the classes are polymorphic and are said to have the same interface.
```python
class ParentClass:
  def print_self(self):
    print('A')

class ChildClass(ParentClass):
  def print_self(self):
    print('B')

>>> obj_A = ParentClass()
>>> obj_B = ChildClass()

>>> obj_A.print_self()
'A'
>>> obj_B.print_self()
'B'
```

## Operator Overloading
Class functions that begin with double underscore __ are called special functions in Python.

```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

>>> p1 = Point(2, 3)
>>> p2 = Point(2,3)
>>> print(p1 + p2)
(3,5)
```

<div class="table-responsive">
	<table border="0">
		<tbody>
			<tr>
				<th>Operator</th>
				<th>Expression</th>
				<th>Internally</th>
			</tr>
			<tr>
				<td>Addition</td>
				<td><code>p1 + p2</code></td>
				<td><code>p1.__add__(p2)</code></td>
			</tr>
			<tr>
				<td>Subtraction</td>
				<td><code>p1 - p2</code></td>
				<td><code>p1.__sub__(p2)</code></td>
			</tr>
			<tr>
				<td>Multiplication</td>
				<td><code>p1 * p2</code></td>
				<td><code>p1.__mul__(p2)</code></td>
			</tr>
			<tr>
				<td>Power</td>
				<td><code>p1 ** p2</code></td>
				<td><code>p1.__pow__(p2)</code></td>
			</tr>
			<tr>
				<td>Division</td>
				<td><code>p1 / p2</code></td>
				<td><code>p1.__truediv__(p2)</code></td>
			</tr>
			<tr>
				<td>Floor Division</td>
				<td><code>p1 // p2</code></td>
				<td><code>p1.__floordiv__(p2)</code></td>
			</tr>
			<tr>
				<td>Remainder (modulo)</td>
				<td><code>p1 % p2</code></td>
				<td><code>p1.__mod__(p2)</code></td>
			</tr>
			<tr>
				<td>Bitwise Left Shift</td>
				<td><code>p1 &lt;&lt; p2</code></td>
				<td><code>p1.__lshift__(p2)</code></td>
			</tr>
			<tr>
				<td>Bitwise Right Shift</td>
				<td><code>p1 &gt;&gt; p2</code></td>
				<td><code>p1.__rshift__(p2)</code></td>
			</tr>
			<tr>
				<td>Bitwise AND</td>
				<td><code>p1 &amp; p2</code></td>
				<td><code>p1.__and__(p2)</code></td>
			</tr>
			<tr>
				<td>Bitwise OR</td>
				<td><code>p1 | p2</code></td>
				<td><code>p1.__or__(p2)</code></td>
			</tr>
			<tr>
				<td>Bitwise XOR</td>
				<td><code>p1 ^ p2</code></td>
				<td><code>p1.__xor__(p2)</code></td>
			</tr>
			<tr>
				<td>Bitwise NOT</td>
				<td><code>~p1</code></td>
				<td><code>p1.__invert__()</code></td>
			</tr>
		</tbody>
	</table>
</div>

<div class="table-responsive">
	<table border="0">
		<tbody>
			<tr>
				<th>Operator</th>
				<th>Expression</th>
				<th>Internally</th>
			</tr>
			<tr>
				<td>Less than</td>
				<td><code>p1 &lt; p2</code></td>
				<td><code>p1.__lt__(p2)</code></td>
			</tr>
			<tr>
				<td>Less than or equal to</td>
				<td><code>p1 &lt;= p2</code></td>
				<td><code>p1.__le__(p2)</code></td>
			</tr>
			<tr>
				<td>Equal to</td>
				<td><code>p1 == p2</code></td>
				<td><code>p1.__eq__(p2)</code></td>
			</tr>
			<tr>
				<td>Not equal to</td>
				<td><code>p1 != p2</code></td>
				<td><code>p1.__ne__(p2)</code></td>
			</tr>
			<tr>
				<td>Greater than</td>
				<td><code>p1 &gt; p2</code></td>
				<td><code>p1.__gt__(p2)</code></td>
			</tr>
			<tr>
				<td>Greater than or equal to</td>
				<td><code>p1 &gt;= p2</code></td>
				<td><code>p1.__ge__(p2)</code></td>
			</tr>
		</tbody>
	</table>
</div>
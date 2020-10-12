

## Interface vs. Abstract Class
# Interfaces
1. Cannot be instantiated. Can be referenced.
2. A class can implement more than one interface. An interface can extends another interface or interfaces (more than one interface).
3. A class that implements interface must implements all the methods in interface.
4. All the methods are public and abstract. And all the fields are public, static, and final.
5. It is used to achieve multiple inheritance.
6. It is used to achieve loose coupling.


# Abstract Class

1. Cannot be created. Can be referenced.
2. Can contain constructors. Constructor of an abstract class is called when an instance of an inherited class is created.
3. Abstract class without an abstract method.
4. Can have methods that cannot be overridden.
5. Instantiation is not possible.


# Interface vs. Abstract Class
- Type of methods: Interface can have only abstract methods. Abstract class can have abstract and non-abstract methods. From Java 8, it can have default and static methods also.
- Final Variables: Variables declared in a Java interface are by default final. An abstract class may contain non-final variables.
- Type of variables: Abstract class can have final, non-final, static and non-static variables. Interface has only static and final variables.
- Implementation: Abstract class can provide the implementation of interface. Interface can’t provide the implementation of abstract class.
- Inheritance vs Abstraction: A Java interface can be implemented using keyword “implements” and abstract class can be extended using keyword “extends”.
- Multiple implementation: An interface can extend another Java interface only, an abstract class can extend another Java class and implement multiple Java interfaces.
- Accessibility of Data Members: Members of a Java interface are public by default. A Java abstract class can have class members like private, protected, etc.
- Consider using abstract classes if any of these statements apply to your situation:

In java application, there are some related classes that need to share some lines of code then you can put these lines of code within abstract class and this abstract class should be extended by all these related classes.
You can define non-static or non-final field(s) in abstract class, so that via a method you can access and modify the state of Object to which they belong.
You can expect that the classes that extend an abstract class have many common methods or fields, or require access modifiers other than public (such as protected and private).
Consider using interfaces if any of these statements apply to your situation:

It is total abstraction, All methods declared within an interface must be implemented by the class(es) that implements this interface.
A class can implement more than one interface. It is called multiple inheritance.
You want to specify the behavior of a particular data type, but not concerned about who implements its behavior.
# Basics

## Variables
- Expressions that refer to a memory location is called **lvalue** expression. An lvalue may appear as either the left-hand or right-hand side of an assignment.
- The term **rvalue** refers to a data value that is stored at some address in memory. An rvalue is an expression that cannot have a value assigned to it which means an rvalue may appear on the right- but not left-hand side of an assignment.
- Define constants:
  - **#define** preprocessor
  - **const** keyword
- Type Qualifiers
  - Objects of type **const** cannot be changed by your program during execution.
  - Declaring a variable **volatile** directs the compiler that the variable can be changed externally. Hence avoiding compiler optimization on the variable reference.
  - A pointer qualified by **restrict** is initially the only means by which the object it points to can be accessed.
- Storage classes
  - **Storage class** specifies the life or scope of symbols such as variable or functions.
  - Class names: auto, static, extern, register and mutable


### Reference Variable
A reference variable is an alias name for the existing variable. Which mean both the variable name and reference variable point to the same memory location. Therefore updation on the original variable can be achieved using reference variable too.

## Functions

### Passing Parameters to Functions
- **Call by value** We send only values to the function as parameters. We choose this if we do not want the actual parameters to be modified with formal parameters but just used.
- **Call by address** We send address of the actual parameters instead of values. We choose this if we do want the actual parameters to be modified with formal parameters.
- **Call by reference** −** The actual parameters are received with the C++ new reference variables as formal parameters. We choose this if we do want the actual parameters to be modified with formal parameters.

### Pointers vs. Reference
- You cannot have NULL references. You must always be able to assume that a reference is connected to a legitimate piece of storage.
- Once a reference is initialized to an object, it cannot be changed to refer to another object. Pointers can be pointed to another object at any time.
- A reference must be initialized when it is created. Pointers can be initialized at any time.

# Object-Oriented

### Class
A class is a blue print which reflects the entities attributes and actions. Technically defining a class is designing an user defined data type.
- A **constructor** is the member function of the class which is having the same as the class name and gets executed automatically as soon as the object for the respective class is created.
- A **destructor** is the member function of the class which is having the same name as the class name and prefixed with tilde (~) symbol. It gets executed automatically w.r.t the object as soon as the object loses its scope. It cannot be overloaded and the only form is without the parameters.
- A **copy constructor** is the constructor which take same class object reference as the parameter. It gets automatically invoked as soon as the object is initialized with another object of the same class at the time of its creation.
- A **virtual destructor** ensures that the objects resources are released in the reverse order of the object being constructed w.r.t inherited object.
### Object
An instance of the class is called as object.

### Static Member Function
- A **static variable** does exit though the objects for the respective class are not created. Static member variable share a common memory across all the objects created for the respective class. A static member variable can be referred using the class name itself.
- A **static member** function can be invoked using the class name as it exits before class objects comes into existence. It can access only static members of the class.



## Encapsulation
The process of binding the data and the functions acting on the data together in an entity (class).
### Access Modifiers
1. Public: All class members will be available to everyone.
2. Private: Class members declared as private can be access only by the functions inside the class.
3. Protected: Class member declared as Protected are inaccessible outside the class but they can be accessed by any subclass (derived class) of that class.
<pre>
<code>
class Parent:
{
    protected:
        int parent_id;
};

class Child : public Parent
{
    public:
    void set_id(int i)
    {
        parent_id = id;
    }
    void display_id()
    {
        cout >> parent_id >> endl;
    }
}
</code>
</pre>
- **Friend class** can access private and protected members of other class in which it is declared as friend.

## Abstraction
Refers to hiding the internal implementation and exhibiting only the necessary details.
- In classes: A class can decide with data member will be visible to the outside world and which is not.
- In header files: Example is pow() method. User will use function pow() without knowing the underlying algorithm.
- Advantages:
  - Helps user to avoid writing the low level code.
  - Avoids code duplication and increases reusability.
  - Can change internal implementation of class indepedently without affecting the user.
  - Increases security of application.
  
## Inheritance
The process of acquiring the properties of the exiting class into the new class. The existing class is called as base/parent class and the inherited class is called as derived/child class.
- Base Class and Derived Class
  - A derived class can access all non-private members of base class.
  - A derived class inherits all base class methods except:
    - Constructors, destructors, and copy constructors
    -  Overloaded operators
    -  Friend functions

- Types of Inheritance
  - Public: All **public and protected** base class members become **public and protected** derived class members, respectively.
  - Protected: All **public and protected** base class members become **protected** derived class members.
  - Private: All **public and protected** base class members become **private** derived class members.
- Advantages: 
  - Code reusability and readability. When child class inherits the properties and functionality of parent class, we need not to write the same code again in child class. This makes it easier to reuse the code, makes us write the less code and the code becomes much more readable.
  
## Polymorphism
1. Compile Time Polymorphism <br>
   - Function Overloading: Defining several functions with the same name with unique list of parameters.
   - Operator Overloading: Defining a new job for the existing operator w.r.t the class objects. An example is s1.concat(s2) and overrloading with operator '+'
2. Runtime Polymorphism
   - Function Overriding: A derived class has a definition for one of the member functions of the base class.
<pre>
    <code>
    class base
    {
        public:
            virtual void print() {}
            void show() {}
    };
    class derived : public base
    {
        public:
            void print() {}
            void show() {}
    };

    int main()
    {
        base * bptr;
        derived d;
        bptr = &d;
        bptr->print(); // virtual func, runtime
        bptr->show(); // non-virtual func, compile time
        return 0;
    }
    </code>
</pre>

## Interface
An interface describes the behavior or capabilities of a C++ class without committing to a particular implementation of that class.
- The C++ interfaces are implemented using **abstract classes** (should not be confused with data abstraction which is a concept of keeping implementation details separate from associated data).
## Abstract Class
- A class is made abstract by declaring at least one of its functions as pure virtual function. A **pure virtual function** is specified by placing "= 0" in its declaration.
- The purpose of an abstract class is to provide an appropriate base class from which other classes can inherit. 
- Abstract classes cannot be used to instantiate objects and serves only as an interface. Attempting to instantiate an object of an abstract class causes a compilation error.
- If a subclass of an ABC needs to be instantiated, it has to implement each of the virtual functions, which means that it supports the interface declared by the ABC. Failure to override a pure virtual function in a derived class, then attempting to instantiate objects of that class, is a compilation error.
### Interface vs. Abstract Class
An abstract class allows you to create functionality that subclasses can implement or override. An interface only allows you to define functionality, not implement it. And whereas a class can extend only one abstract class, it can take advantage of multiple interfaces.

# Exception Handling
- **try, catch, and throw**
- If an exception is thrown outside by a try block, then the program shall quit abruptly.

# Dynamic Memory
Memory in your C++ program is divided into two parts:
1. Stack: All variables declared inside the function will take up memory from the stack.
2. Heap: This is unused memory of the program and can be used to allocate the memory dynamically when program runs.

- **New operator** allocate memory at run time within the heap for the variable of a given type using a special operator in C++ which returns the address of the space allocated.
  - We cannot resize the allocated memory which was allocated.
- **Delete operator** de-allocates memory that was previously allocated by new operator. 
  - **Delete[]** is used to release the array allocated memory which was allocated using new[] and **delete** is used to release one chunk of memory which was allocated using new.
- The **malloc()** function from C, still exists in C++, but it is recommended to avoid using malloc() function. The main advantage of new over malloc() is that new doesn't just allocate memory, it constructs objects which is prime purpose of C++.
- **Shallow copy** does memory dumping bit-by-bit from one object to another. **Deep copy** is copy field by field from object to another. Deep copy is achieved using copy constructor and or overloading assignment operator.

# Namespaces
A namespace is the logical division of the code which can be used to resolve the name conflict of the identifiers by placing them under different name space.
- **'Using' keyword** is to tell the compiler that the subsequent code is making use of the names in the specified namespace.

# Preprocessor
Preprocessor is a directive to the compiler to perform certain things before the actual compilation process begins.
- **Macros** are implemented with the <code>#define</code> keyword. All subsequent occurrences of macro in that file will be replaced by the defined text before the program is compiled.
- If a header file is included with in < > then the compiler searches for the particular header file only with in the built in include path. If a header file is included with in “ “, then the compiler searches for the particular header file first in the current working directory, if not found then in the built in include path.
- A function prefixed with the keyword inline before the function definition is called as **inline function**. The inline functions are faster in execution when compared to normal functions as the compiler treats inline functions as macros.
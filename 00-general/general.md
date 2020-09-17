
## Four Pillars of Object-Oriented Programming
### Encapsulation
Binding together data and the functions that manipulate them.
```
```

### Abstraction
Providing only essential information about data while hiding the details or implementation.
### Inheritance
Ability of a class to derive properties and characteristics from another class.
### Polymorphism
Define one interface and have multiple implementations.
- Polymorphism with class methods:
```
```
- Polymorphism with Inheritance
```
```
- Polymorphism with Function:
```
```
- Polymorphism with Function and Objects:
```
```

## S.O.L.I.D Principles
### Single Responsibility Principle
A class should have a single job.
```
    class User:
    def __init__(self, name: str):
        self.name = name
    def get_name(self)->str:
        pass
    def save(self, user: User):
        pass
```
### Open-Closed Principle
Open for extension, not modification.
### Liskov Substitution Principle
Classes are completely isolated and unaware of changes in the class hierarchy.
### Interface Segregation Principle
### Dependency Inversion Principle
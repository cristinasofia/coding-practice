
## Four Pillars of Object-Oriented Programming
1. Encapsulation
    Binding together data and the functions that manipulate them.
2. Abstraction
    Providing only essential information about data while hiding the details or implementation.
3. Inheritance
    Ability of a class to derive properties and characteristics from another class.</p>
4. Polymorphism
    Define one interface and have multiple implementations.
    <ul>
        <li>
            <p>Polymorphism with class methods:</p>
            <pre>
            <code>
            class Father():
            </code>
            </pre>
        </li>
        <li>
            <p>Polymorphism with Inheritance</p>
                <pre>
                <code>
                class Bird():
                </code>
                </pre>
        </li>
        <li>
            <p>Polymorphism with Function:</p>
                <pre>
                <code>
                class Bird():
                </code>
                </pre>
        </li>
        <li>
            <p>Polymorphism with Function and Objects:</p>
                <pre>
                <code>
                class Bird():
                </code>
                </pre>
        </li>
    </ul>
## S.O.L.I.D Principles
1. Single Responsibility Principle
A class should have a single job.
<pre>
<code>
    class User:
    def __init__(self, name: str):
        self.name = name
    def get_name(self)->str:
        pass
    def save(self, user: User):
        pass
</code>
</pre>
2. Open-Closed Principle
    Open for extension, not modification.
3. Liskov Substitution Principle
    Classes are completely isolated and unaware of changes in the class hierarchy.
4. Interface Segregation Principle
5. Dependency Inversion Principle
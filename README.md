# Object Oriented Scalable Calculator
A simple OO calculator, built with the focus of extreme scalability, allowing new operations to be added with ease.

The goal of this project was to create a calculator in a world where new operations are invented and changed every day (operations referring to addition, subtraction, and other similar calculations). A calculator in this world would need to be modifiable in as few lines as possible. In order to achieve this, this program uses OO and abstraction techniques to be easily changable and scalable, only requiring one symbol to be altered in order to change an operation, and one class to be added to create a new one.

# Structure 
calculator.py contains all logic of the calculator.
calctest.py contains tests for calculator.py.
calculatorgui.py opens a GUI for the calculator.

# Instructions
Run 
```
python3 .\calculatorgui.py  
```
Or otherwise run the calculatorgui.py file to start the GUI

# Examples
The code is flexible enough to easily build new custom operators. As an example of this, the '#' key on the calculator is a unique operator that adds the sum and product of the numbers adjacent to it.
```
class AddMultiply(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '#'
        self.priority = 2

    def operate(self):
        return [self.x + self.y + self.x * self.y]
```
```
Enter Equation: 3#2
11
```
There are many other unique example operations within the code as proofs of concept, such as the parentheses [], which function as brackets (), however with a lower priority.

As mentioned earlier the project is very easily modified. Below is the class responsible for addition. To change the symbol or priority (the order in which operations are executed) only this class needs to be modified.
```
class Add(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '+'
        self.priority = 1
```
```
Enter Equation: 1+1
2
```

```
class Add(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  'A'
        self.priority = 1
```
```
Enter Equation: 1A1
2
```

Below is an example of changing the priority of operations such that they occur in reverse order.
```
class Add(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '+'
        self.priority = 1

class Multiply(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '*'
        self.priority = 2
```
```
Enter Equation: 1+1*3
4
```

```
class Add(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '+'
        self.priority = 2

class Multiply(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '*'
        self.priority = 1
```
```
Enter Equation: 1+1*3
6
```
This applies to every operation, with all of them being modifiable with a single line change.

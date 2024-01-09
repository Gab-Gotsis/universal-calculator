# Object Oriented Scalable Calculator
An OO calculator, built with the focus of extreme scalability, allowing new operations to be added with ease.

The goal of this project was to create a calculator in a world where new operations are invented every day. Operations in this case referring to addition, subtraction, and other similar calculations. In order to achieve this, this program uses OO and abstraction techniques to be easily changable and scalable.

# Examples
Below is the class responsible for addition. To change the symbol, priority (the order in which operations are executed) only this class needs to be modified.
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
        self.operator =  '#'
        self.priority = 1
```
```
Enter Equation: 1#1
2
```
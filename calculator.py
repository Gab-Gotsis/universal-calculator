#Define mathematical operators and parenthesis as classes
#Operator is the parent class of all operators
class Operator:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y  

    def operate(self):
        pass
    
    def findOperation(self, operation):
        for subclass in Operator.__subclasses__():
            if operation == subclass().operator:
                return subclass
        return None

class Add(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '+'
        self.priority = 1
    def operate(self):
        return [self.x + self.y]

class Subtract(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '-'
        self.priority = 1
    def operate(self):
        return [self.x - self.y]

class Multiply(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '*'
        self.priority = 2
    def operate(self):
        return [self.x * self.y]

class Divide(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '/'
        self.priority = 2

    def operate(self):
        if self.y == 0:
            print("error, can't divide by 0")
            return "error"
        return [self.x / self.y]

class Exponent(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '^'
        self.priority = 3

    def operate(self):
        return [self.x ** self.y]
    
class AddMultiply(Operator):
    def __init__(self, x=0, y=0):
        super().__init__(x,y)
        self.operator =  '#'
        self.priority = 2

    def operate(self):
        return [self.x + self.y + self.x * self.y]
    
#Parenthesis is the parent class of all parenthesis
class Parenthesis():
    def __init__(self, index=0, equation=0):
        self.index = index
        self.contained = equation

    def findOperation(self, operation):
        for subclass in Parenthesis.__subclasses__():
            if operation == subclass().operator:
                return subclass
        return None
    
    def operate(self):
        index = self.index
        equation = self.contained
        start = index
        end = 0
        numseen = 0
        for i in range(index+1, len(equation)):
            if equation[i] == self.operator:
                numseen += 1
            if equation[i] == self.closeoperator:
                if numseen == 0:
                    end = i
                    break
                else:
                    numseen -= 1
        subsection = equation[start+1:end] 
        return equation[:start] + solve(subsection) + equation[end+1:] 
    
class Brackets(Parenthesis):
    def __init__(self, index=0, equation=0):
        super().__init__(index, equation)
        self.operator =  '('
        self.closeoperator = ')'
        self.priority = 4  

class Pipe(Parenthesis):
    def __init__(self, index=0, equation=0):
        super().__init__(index, equation)
        self.operator =  '['
        self.closeoperator = ']'
        self.priority = 3

#the symbols of numbers changing is beyond the scope of this project, so we can hard code it
numbers = ['0','1','2','3','4','5','6','7','8','9', '.']

#Return the priority of the symbol
def priority(symbol):
    if Operator().findOperation(symbol) != None:
        return Operator().findOperation(symbol)().priority
    if Parenthesis().findOperation(symbol) != None:
        return Parenthesis().findOperation(symbol)().priority
    else:
        return 0

#Modify the input to be in a format that can be solved
def modifyInput(input):
    equation = ""
    for symbol in str(input):
        if symbol not in numbers:
            equation += " " + symbol + " "
        else:
            equation += symbol
    equation = equation.split()
    return equation

#Solve the equation
def solve(equation):
    for i in range(5,0,-1):
        for symbol in equation:
            if symbol in equation and priority(symbol) == i:
                parenthesis = Parenthesis().findOperation(symbol)
                if parenthesis != None:
                    equation = parenthesis(equation.index(symbol), equation).operate()
                else:
                    index = equation.index(symbol)
                    equation = calculate(symbol, index, equation)
    return equation

#Performs operand logic
def calculate(operator, index, equation):
    x = float(equation[index-1])
    y = float(equation[index+1])
    operation = Operator().findOperation(operator)
    return equation[:index-1] + operation(x,y).operate() + equation[index+2:]

#removes unnecessary dot points and rounds to 3 decimal places
def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return round(num, 3)  


#Uncomment the following lines to input equation through terminal:
  
#input = input("Enter Equation: ")
#print(formatNumber(solve(modifyInput(input))[0]))




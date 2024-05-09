from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
# 1.

def reverseString(string:str) -> str:
    s = Stack()
    for char in string :
        s.push(char)
        
    reString = ""
    while not s.is_empty() :
        reString += s.pop()
        
    return reString

print("1.", reverseString("We will conquere COVID-19"))

# 2.
# "{}',"()" or "[]"
def is_balanced(string:str) -> bool:
    parantheses = {"}":"{", ")":"(", "]":"["}
    stack = Stack()
    for char in string :
        if char in list(parantheses.values()) :
            # if char is open parantheses
            stack.push(char)
        if char in list(parantheses.keys()) :
            # if char is close parantheses
            # if parantheses close before open
            if stack.is_empty() : return False
            
            # if parantheses close don't match with open parantheses
            pop = stack.pop()
            if pop != parantheses.get(char) : return False
            
    return True

print("2.")
print(is_balanced("({a+b})"))     # --> True
print(is_balanced("))((a+b}{"))   # --> False
print(is_balanced("((a+b))"))     # --> True
print(is_balanced("))"))          # --> False
print(is_balanced("[a+b]*(x+2y)*{gg+kk}")) # --> True

class Employee :
    # __init__ == constructor of classes
    # create attribute by self.attributeName = value
    # every behavior required "self" argument
    def __init__(self, id: int, n: str) -> None:
        self.name = n
        self.id = id
        
    def display(self) :
        print(f"id: {self.id}, name: {self.name}")
        
    def delete(self) -> None :
        del self.id
        del(self)
        
emp = Employee(1, "coder")

emp.display()

emp.delete()

try :
    emp.display()
except Exception as e :
    print(type(e).__name__)
    print(e)

del emp

try :
    emp.display()
except Exception as e :
    print(type(e).__name__)
    print(e)
class AdultException(Exception) :
    # creating exception class required extended "Exception"
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
    def showException(self) -> None:
        print("AdultExecption:", self.args[0])
        
class Person :
    def __init__(self, n: str, a: int) -> None:
        self.name = n
        self.age = a
        
    def get_minor_age(self) -> int:
        if self.age>18 :
            return self.age
        else :
            # using exception by "raise" the "Exception" class
            raise AdultException("You are not reach 18...")
        
    def display_person(self) -> None:
        print(f"Name: {self.name}")
        # deal with exception occured by try-except( try-catch )
        try :
            print(f"Age: {self.get_minor_age()}")
        except AdultException as ae :
            ae.showException()
            
            
p = Person("Hu", 19)
p.display_person()
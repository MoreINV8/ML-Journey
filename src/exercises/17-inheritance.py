class Animal :
    def __init__(self, n: str, a: int) -> None:
        self.name = n
        self.age = a
        
    def introduce(self) -> None:
        print(f"My name is {self.name}.Now I'm {self.age} year-old.")
        
    def eat(self) -> None:
        print(f"{self.name} is eating...")
        
class Dog(Animal) :
    # inherit class by SubClass(SuperClass)
    def __init__(self, n: str, a: int) -> None:
        super().__init__(n=n, a=a)
        
    def bark(self) -> None:
        print("WOOF WOOF !!")
        
d = Dog("gogo", 4)
d.introduce()
d.bark()
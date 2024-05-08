KEY = 0
DATA = 1

class HashMap :
    def __init__(self) -> None:
        self.MAX:int = 10
        
    def hashed(self, key:str) -> int:
        coded = 0
        for char in key :
            coded += ord(char)
            
        return coded  % self.MAX
    
class Chaining(HashMap) :
    def __init__(self) -> None:
        super().__init__()
        self.arr:list[list[tuple[str, object]]] = [[] for i in range(self.MAX)]
        
    def __setitem__(self, key:str, value:object) -> None:
        coded = self.hashed(key= key)
        slot = self.arr[coded]
        
        founded = False
        for index, element in enumerate(slot) :
            if len(element) == 2 and element[KEY] == key :
                slot[index] = (key, value)
                founded = True
                break
        
        if not founded :
            slot.append((key, value))
            
    def __getitem__(self, key:str) -> object:
        coded = self.hashed(key= key)
        
        for element in self.arr[coded] :
            if len(element) == 2 and element[KEY] == key :
                return element[DATA]
            
        raise Exception("unexpected key...")
    
    def __delitem__(self, key:str) -> None:
        coded = self.hashed(key= key)
        
        for index, element in enumerate(self.arr[coded]) :
            if len(element) == 2 and element[KEY] == key :
                del self.arr[coded][index]
                return
                
        raise Exception("unexpected key...")
    
    def contains(self, key:str) -> bool:
        coded = self.hashed(key= key)
        
        for element in self.arr[coded] :
            if len(element) == 2 and element[KEY] == key :
                return True
            
        return False
    
class Linear(HashMap) :
    def __init__(self) -> None:
        super().__init__()
        self.arr = [None for i in range(self.MAX)]
        self.stored = 0
    
    def __setitem__(self, key:str, value:object) -> None:
        if self.stored == self.MAX :
            raise Exception("storage full...")
        
        i = self.hashed(key= key)
        while not self.arr[i] is None and self.arr[i][KEY] != key :
            i += 1
            if i == self.MAX :
                i = 0
             
        if self.arr[i] is None :   
            self.stored += 1
        self.arr[i] = (key, value)
                
    def __getitem__(self, key:str) -> object:
        coded = self.hashed(key= key)
        i = coded
        while not self.arr[i] is None :
            if (self.arr[i][KEY] == key) :
                return self.arr[i][DATA]
            i += 1
            if i == coded :
                break
            if i == self.MAX :
                i = 0
                
        raise Exception("unexpected key...")
    
    def __delitem__(self, key:str) -> None:
        coded = self.hashed(key= key)
        i = coded
        while not self.arr[i] is None :
            if self.arr[i][KEY] == key :
                self.arr[i] = None
                self.stored -= 1
                return
            i += 1
            if i == coded :
                break
            if i == self.MAX :
                i = 0
                
        raise Exception("unexpected key...")
    

temp = Linear()
with open("data/nyc_weather.csv") as weather :
    for i, line in enumerate(weather) :
        if i == 0 : continue
        tokens = line.rstrip("\n").split(",")
        date = tokens[0]
        temperature = tokens[1]
        temp[date] = int(temperature)
        
print(temp.arr)

# 1.
sumTemp = sum([temp[f"Jan {i + 1}"] for i in range(7)])
print("1.1.", sumTemp/7)
maxTemp = max([temp[f"Jan {i + 1}"] for i in range(10)])
print("1.2.", maxTemp)

# 2.
print("2.1.", temp["Jan 9"])
print("2.2.", temp["Jan 4"])

# 3.
words = Chaining()
with open("data/poem.txt") as poem :
    for line in poem :
        tokens = line.rstrip("\n").split()
        for word in tokens :
            if words.contains(word) :
                words[word] += 1
            else :
                words[word] = 1
                
print("3.")
for elements in words.arr :
    for element in elements :
        print(f"'{element[KEY].ljust(15)}': {element[DATA]}")
        
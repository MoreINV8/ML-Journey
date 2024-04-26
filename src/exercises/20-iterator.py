class FiboSequence() :
    def fibo(self, num: int) -> None:
        """create a sequence of fibonacci number up to num

        Args:
            num (int): limited of fibonacci sequence

        Returns:
            list[int]: a sequence of fibonacci
        """
        stored = [0, 1]
        for i in range(2, num + 1) :
            stored.append(stored[i - 1] + stored[i - 2])
            
        self.sequence = stored
    
    def __init__(self, num: int) -> None:
        self.fibo(num)
        self.index = -1
        
    # using "iter()" required implementing "__iter__(self)"
    def __iter__(self):
        return self
    
    # using "next()" required implementing "__next__(self)"
    def __next__(self) -> int:
        self.index += 1
        if (self.index == len(self.sequence)) :
            raise StopIteration
        
        return self.sequence[self.index]
        
f = FiboSequence(5)

print(f.sequence)

itr = iter(f)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
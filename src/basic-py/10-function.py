# 1.

def calculate_area(base:int, height:int) -> float :
    return base * height / 2

print("1.", "base = 4, height = 3 :", calculate_area(base = 4, height = 3))

# ------------------------------------
# 2.
print("2.--------")

def calculate_area2(height:float, base:float = -1, width:float = -1) -> float :
    if base == -1 and width != -1 :
        return height * width
    elif width == -1 and base != -1 :
        return height * base / 2
    raise ValueError

print("base = 4, height = 3 :", calculate_area2(base = 4, height = 3))
print("width = 4, height = 3 :", calculate_area2(width = 4, height = 3))

# ------------------------------------
# 3.
print("3.--------")

def printStar(height:int) -> None :
    for i in range(1, height + 1) :
        print("*" * i)
        
printStar(3)
printStar(4)
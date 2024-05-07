# if doesn't have if statment while call "area" from another file will perfrom the statment

def findArea(width:float, height:float) -> float :
    print(f"__name__ = {__name__}")
    return width * height

if __name__ == "__main__" :
    print(findArea(3, 4))

# ↕

# meaning same as 
# int main() {
#    print(findArea(a,b))
# }
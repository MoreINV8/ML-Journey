# have ability like iterator but don't need to wirte __iter__, __next__ and don't need to raise exception
def power() :
    i = 1
    while True :
        # using "yield" to work like return but will continue after when iteration
        yield i * i
        i += 1
        
for i in power() :
    if i > 100 :
        break
    print(i)
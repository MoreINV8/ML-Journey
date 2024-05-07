# 1.

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

getHead = 0
for item in result :
    if (item == "heads") :
        getHead += 1
        
print("1.", getHead)

# ------------------------------------
# 2.
print("2.--------")

for i in range(1, 11) :
    if i % 2 == 1 :
        print(i ** 2)
        
# ------------------------------------
# 3.
print("3.--------")

mounth = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
expenseList = [-1] * 12

maxLen = max([len(i) for i in mounth])

for i in range(len(mounth)) :
    # exp = int(input(f"Input expense in {mounth[i]} :"))
    exp = -1
    if exp == -1 :
        continue
    expenseList[i] = exp
    
for i in range(len(mounth)) :
    if expenseList[i] == -1 :
        print(f"{mounth[i].ljust(maxLen)}: Not found")
    else :
        print(f"{mounth[i].ljust(maxLen)}: {expenseList[i]} dollar")
        
# ------------------------------------
# 4.
print("4.--------")

finish = True
for i in range(1, 6) :
    print("walked 1 km...")
    ans = input("Are you tried?: (Y/N)")
    if ans == "Y" :
        finish = not finish
        break
    
if finish :
    print("Congratulations, you walked 5 km !!!")
    
# ------------------------------------
# 5.
print("5.--------")

for i in range(1, 6) :
    print("*" * i)
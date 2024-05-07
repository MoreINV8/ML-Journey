# 1.

mounth = ["January", "February", "March", "April", "May"]
expense = [2200, 2350, 2600, 2130, 2190]

print("1.1.", expense[1] - expense[0])

tolQuater = 0
for i in range(3) :
    tolQuater += expense[i]
print("1.2.", tolQuater)

exact = None
for i in expense :
    if i == 2000 :
        exact = i
        break
ans = "None"
if exact != None :
    ans = mounth[exact]
print("1.3.", ans)

mounth.append("June")
expense.append(1980)
print("1.4.", expense)

april = 3
expense[april] -= 200
print("1.5.", expense)

print("------------------------------")

# 2.

heros=['spider man','thor','hulk','iron man','captain america']

length = 0
for i in heros :
    length += 1
print("2.1.", length)

heros.append("black panther")
print("2.2.", heros)

heros.remove("black panther")
heros.insert(3, "black panther")
print("2.3.", heros)

heros.remove("thor")
heros.remove("hulk")
heros.insert(1, "doctor strange")

# heros[1:3] = "doctor strange"

print("2.4.", heros)

heros.sort()
print("2.5.", heros)

print("------------------------------")

# 3.

maxNum = int(input("input max number: "))
oddNums = []

for i in range(1, maxNum + 1) :
    if i % 2 != 0 :
        oddNums.append(i)
        
print("3.", oddNums)

print("------------------------------")
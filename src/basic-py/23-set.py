# 1.

listNum = [1, 2, 3, 4, 5, 3, 5, 4, 5, 2, 5]

# frozenset can't be change ( cannot add, remove, ... )
fs = frozenset(listNum)
print("1.", fs)

# -----------------------
# 2.

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print("2.", set1 - set2)
# 1.

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

binary_dict = {num:bi for num, bi in zip(integer, binary)}

print("1.", binary_dict)

# --------------------------------
# 2.

integer2 = [1, -1, 2, 3, 5, 0, -7]
inverse = [i * -1 for i in integer2]

print("2.", inverse)

# --------------------------------
# 3.

integer3 = [1, -1, 2, -2, 3, -3]
uniqe_sqr = {i * i for i in integer3}

print("3.", uniqe_sqr)
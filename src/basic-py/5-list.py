# 1.
print("1.")

expenses: list[int] = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("1.1", expenses[1] - expenses[0])
# 2. Find out your total expense in first quarter (first three months) of the year.
print("1.2", sum(expenses[0:3]))
# 3. Find out if you spent exactly 2000 dollars in any month
print("1.3", 2000 in expenses)
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print("1.4", expenses)
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expenses[3] = expenses[3] - 200
print("1.5", expenses)

# ------------------------------------
# 2.
print("2.")

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. Length of the list
print("2.1", len(heros))
# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print("2.2", heros)
# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
bp = "black panther"
heros.remove(bp)
heros.insert(3, bp)
print("2.3", heros)
# 4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
heros.remove("thor")
heros.remove("hulk")
heros.insert(1, "doctor strange")
print("2.4", heros)
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print("2.5", heros)
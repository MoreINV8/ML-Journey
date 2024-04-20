from math import pi
# 1.
# print("1.--------")

# def printPopulation(populations: dict[str, int]) -> None :
#     maxLen = max([len(k) for k in list(populations.keys())])
#     for key, value in populations.items() :
#         print(f"{key.ljust(maxLen)} ==> {value}")

# populations = {
#     "China": 143,
#     "India": 136,
#     "USA": 32,
#     "Pakistan": 21
# }

# while True :
#     command = input("Enter your command((P)rint, (A)dd, (R)emove, (Q)uery): ")
#     if command == "P" :
#         printPopulation(populations=populations)
#     elif command == "A" :
#         country = input("Enter your country: ")
#         if (populations.get(country) == None) :
#             pop = int(input("Enter population: "))
#             populations[country] = pop
#         else :
#             print("This country is aready exist.")
#     elif command == "R" :
#         country = input("Enter your country: ")
#         if (populations.get(country)) :
#             populations.pop(country)
#             printPopulation(populations=populations)
#         else :
#             print("This country doesn't exist.")
#     elif command == "Q" :
#         country = input("Enter your country: ")
#         if (populations.get(country)) :
#             print(populations[country])
#         else :
#             print("This country doesn't exist.")
#     else :
#         break
    
# ------------------------------------
# 2.
# print("2.--------")

# stocks = {
#     "info": [600,630,620],
#     "ril": [1430,1490,1567],
#     "mtl": [234,180,160]
# }

# while True :
#     command = input("Enter your command((P)rint, (A)dd): ")
#     if command == "P" :
#         for k, v in stocks.items() :
#             print(f"{k} ==> {v} ==> avg: {sum(v)/len(v):.2f}")
#     elif command == "A" :
#         ticker = input("Enter stock ticker: ")
#         price = int(input("Enter stock price: "))
#         if (stocks.get(ticker)) :
#             stocks[ticker].append(price)
#         else :
#             stocks[ticker] = [price]
#     else :
#         break
    
# ------------------------------------
# 3.
print("3.--------")

def circle_calc(radius:float) -> tuple[float, float, float] :
    area = pi * radius**2
    circumference = 2 * pi * radius
    diameter = 2 * radius
    return (area, circumference, diameter)

calculated = circle_calc(7)
print(f"radius = 7: area = {calculated[0]:.2f}, circum = {calculated[1]:.2f}, dia = {calculated[2]:.2f}")

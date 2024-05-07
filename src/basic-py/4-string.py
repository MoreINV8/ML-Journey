# 1.

street = "??"
city = "Osaka"
country = "Japan"

useOperator = "street: " + street + "\ncity: " + city + "\ncountry: " + city
usefString = f"street: {street}\ncity: {city}\ncountry: {country}"

print("1.")
print("using operator \"+\"")
print(useOperator)
print("=====")
print("using fstring")
print(usefString)

# ------------------------------------
# 2.

quote = "Earth revolves around the sun"

print("2.")
print(quote[6:14])
print(quote[26:])

# ------------------------------------
# 3.

fruits = 0
vegetables = 0

print("3.", f"I eat {vegetables} veggies and {fruits} fruits daily")
# ------------------------------------
# 4.

s = 'maine 200 banana khaye'
s = s.replace('200 banana', '10 samosa')

print("4.", s)
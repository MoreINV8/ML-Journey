# 1.
print("1.")

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

def convertCity(cityName: str) -> int :
    atCity = -1
    if (cityName in india) :
        atCity = 0
    elif (cityName in pakistan) :
        atCity = 1
    elif (cityName in bangladesh) :
        atCity = 2
        
    return atCity

countries = ["India", "Pakistan", "Bangladesh"]

# 1.) Write a program that asks user to enter a city name and it should tell which country the city belongs to
print("1.1.")
cityName = input("Enter your city: ")

convertedCity = convertCity(cityName=cityName)

if (convertCity != -1) :
    print(f"{cityName} is in {countries[convertedCity]}.")
else :
    print(f"Base on my data, I don't know where is {cityName}.")

# 2.) Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
print("1.2.")

cityA = input("Enter your first city: ")
cityB = input("Enter your second city: ")

convertedA = convertCity(cityA)
convertedB = convertCity(cityB)

if (convertedA == convertedB) :
    print(f"Both cities are in {countries[convertedA]}.")
else :
    print("They don't belong to same country.")
    
# ------------------------------------
# 2.
print("2.")

getData:bool = False

while not getData :
    try :
        sugarLevel = int(input("Input your recently sugar level: "))
        getData = True
    except ValueError:
        print("Please, input sugar level...")
   
level = "normal"     
if sugarLevel > 100 :
    level = "high"
elif sugarLevel < 80 :
    level = "low"
    
print(f"The sugar is {level}.")
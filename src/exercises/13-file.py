absolutePath = "C:\\Users\\Lenovo\\Documents\\s0me_thing\\ML-en_Journey\\data"

# 1.

f = open(absolutePath + "\\poem.txt", "r")

poem = f.read()

f.close()

poem = poem.split()

wordDict = {}

for word in poem :
    if not wordDict.get(word):
        wordDict[word] = 1
    else :
        wordDict[word] += 1
        
maxWord = []
count = 0

for k, v in wordDict.items() :
    if v > count :
        maxWord = [k]
        count = v
    elif v == count :
        maxWord.append(k)
        
print("1.", maxWord, count)

# ------------------------------------
# 2.

with open(absolutePath + "\\stocks.csv", "r") as stocks_csv :
    stocks = []
    for line in stocks_csv :
        stocks.append(line.rstrip().split(","))
        
calculated = ["Company Name,PE Ratio,PB Ratio"]

for i in range(1, len(stocks)) :
    cname = stocks[i][0]
    pe = "{:.2f}".format(int(stocks[i][1]) / int(stocks[i][2]))
    pb = "{:.2f}".format(int(stocks[i][1]) / int(stocks[i][3]))
    
    line = ",".join([cname, pe, pb])

    calculated.append(line)
    
with open(absolutePath + "\\output.csv", "w") as out :
    for i in calculated :
        out.writelines(f"{i}\n")
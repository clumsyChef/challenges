allChars = [chr(i) for i in range(97, 123)]

mainStr = ""
for i in allChars:
    x = ord(i)
    if(x == 103):
        break
    lastPart = mainStr[:-1]
    mainStr += i
    mainStr += lastPart
    print(mainStr)

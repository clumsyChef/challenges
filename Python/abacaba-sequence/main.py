# ABACABA Sequence
# https://www.reddit.com/r/dailyprogrammer/comments/njxq95/20210524_challenge_391_easy_the_abacaba_sequence/

allChrs = [chr(i) for i in range(97, 123)]

mainStr = ""

count = 0

for i in allChrs:
    mainStr += (i + mainStr)
    print("----------------------")
    print(mainStr)
    print("----------------------")

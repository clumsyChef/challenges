# Link to challenge
# https://www.reddit.com/r/dailyprogrammer/comments/o4uyzl/20210621_challenge_395_easy_nonogram_row/

# nonogramrow([]) => []
# nonogramrow([0,0,0,0,0]) => []
# nonogramrow([1,1,1,1,1]) => [5]
# nonogramrow([0,1,1,1,1,1,0,1,1,1,1]) => [5,4]
# nonogramrow([1,1,0,1,0,0,1,1,1,0,0]) => [2,1,3]
# nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1]) => [2,1,3]
# nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) => [1,1,1,1,1,1,1,1]

def nonogramrow(anArr):
    finalArr = []
    count = 0
    for i in range(len(anArr)):
        el = anArr[i]
        if el == 1:
            count += 1

        if (el == 0) or (i == (len(anArr) - 1)):
            if count != 0:
                finalArr.append(count)
            count = 0

    
    print(finalArr)
    return finalArr



nonogramrow([]) 
nonogramrow([0,0,0,0,0]) 
nonogramrow([1,1,1,1,1]) 
nonogramrow([0,1,1,1,1,1,0,1,1,1,1]) 
nonogramrow([1,1,0,1,0,0,1,1,1,0,0]) 
nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1]) 
nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) 


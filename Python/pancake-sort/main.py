# Pancake Sort
# https://www.reddit.com/r/dailyprogrammer/comments/np3sio/20210531_challenge_392_intermediate_pancake_sort/

#flipfront([0, 1, 2, 3, 4], 2) => [1, 0, 2, 3, 4]
#flipfront([0, 1, 2, 3, 4], 3) => [2, 1, 0, 3, 4]
#flipfront([0, 1, 2, 3, 4], 5) => [4, 3, 2, 1, 0]
#flipfront([1, 2, 2, 2], 3) => [2, 2, 1, 2]
#flipfront([3, 1, 2, 1], 4) => [1, 2, 1, 3]
#flipfront([1, 2, 1, 3], 2) => [2, 1, 1, 3]
#flipfront([2, 1, 1, 3], 3) => [1, 1, 2, 3]



def flipfront(anArr, n):
    ans = list(reversed(anArr[0:n])) + anArr[n:]
    print(ans)
    return None

flipfront([0, 1, 2, 3, 4], 2)
flipfront([0, 1, 2, 3, 4], 3)
flipfront([0, 1, 2, 3, 4], 5)
flipfront([1, 2, 2, 2], 3)
flipfront([3, 1, 2, 1], 4)
flipfront([1, 2, 1, 3], 2)
flipfront([2, 1, 1, 3], 3)

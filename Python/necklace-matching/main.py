# https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

#same_necklace("nicole", "icolen") => true
#same_necklace("nicole", "lenico") => true
#same_necklace("nicole", "coneli") => false
#same_necklace("aabaaaaabaab", "aabaabaabaaa") => true
#same_necklace("abc", "cba") => false
#same_necklace("xxyyy", "xxxyy") => false
#same_necklace("xyxxz", "xxyxz") => false
#same_necklace("x", "x") => true
#same_necklace("x", "xx") => false
#same_necklace("x", "") => false
#same_necklace("", "") => true

def same_necklace(str1, str2):
    if(len(str1) != len(str2)):
        print(False)
        return False
    
    if(len(str1) == 0 and len(str2) == 0):
        print(True)
        return True

    for i in str2:
        str2 = str2[-1:] + str2[:-1]
        if(str1 == str2):
            print(True)
            return True

    print(False)
    return False


same_necklace("nicole", "icolen")
same_necklace("nicole", "lenico")
same_necklace("nicole", "coneli") 
same_necklace("aabaaaaabaab", "aabaabaabaaa")
same_necklace("abc", "cba") 
same_necklace("xxyyy", "xxxyy") 
same_necklace("xyxxz", "xxyxz") 
same_necklace("x", "x")
same_necklace("x", "xx") 
same_necklace("x", "")
same_necklace("", "")





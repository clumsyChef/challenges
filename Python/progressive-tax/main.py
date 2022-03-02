# https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/

#tax(0) => 0
#tax(10000) => 0
#tax(10009) => 0
#tax(10010) => 1
#tax(12000) => 200
#tax(56789) => 8697
#tax(1234567) => 473326


def tax(n):
    a = [10000, 30000, 100000]
    b = [0, 10, 25, 40]
    ib = []
    for i in a:
        k = None    
        if (i > n):
            k = n
        else:
            k = i - sum(ib)
        
        ib.append(k)
        n -= k
        if (k == n):
            break
    
    if (n > 0):
        ib.append(n)
    
    totalTax = 0

    for i in range(len(ib)):
        totalTax += int(ib[i] * (b[i] / 100))
    print(totalTax)


tax(0)
tax(10000)
tax(10009)
tax(10010)
tax(12000)
tax(56789)
tax(1234567)

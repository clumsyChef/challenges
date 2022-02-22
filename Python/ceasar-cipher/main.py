# Ceasar Cipher
# https://www.reddit.com/r/dailyprogrammer/comments/myx3wn/20210426_challenge_387_easy_caesar_cipher/

#caesar("a", 1) => "b"
#caesar("abcz", 1) => "bcda"
#caesar("irk", 13) => "vex"
#caesar("fusion", 6) => "layout"
#caesar("dailyprogrammer", 6) => "jgorevxumxgsskx"
#caesar("jgorevxumxgsskx", 20) => "dailyprogrammer"

def caesar(strr, skip):
    number = [chr(ord(i) + skip) if (ord(i) + skip) < 123 else chr(ord(i) + skip - 26) for i in strr]
    final = "".join(number)
    print(final)

caesar("a", 1)
caesar("abcz", 1)
caesar("irk", 13)
caesar("fusion", 6)
caesar("dailyprogrammer", 6)
caesar("jgorevxumxgsskx", 20)

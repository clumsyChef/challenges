# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

#lettersum("") => 0
#lettersum("a") => 1
#lettersum("z") => 26
#lettersum("cab") => 6
#lettersum("excellent") => 100
#lettersum("microspectrophotometries") => 317


def lettersum(word):
    sum = 0
    for i in word:
        code = ord(i) - 96
        sum += code

    print(sum);


lettersum("")
lettersum("a")
lettersum("z")
lettersum("cab")
lettersum("excellent")
lettersum("microspectrophotometries")

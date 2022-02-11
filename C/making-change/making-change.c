// MAKING CHANGE
// https://www.reddit.com/r/dailyprogrammer/comments/nucsik/20210607_challenge_393_easy_making_change/

#include <stdio.h>
#include <stdlib.h>

int change(unsigned int paisa);

int main() {
    //change(0) => 0
    //change(12) => 3
    //change(468) => 11
    //change(123456) => 254
    unsigned int thisChange = change(12);
    printf("%d", thisChange);
    return 0;
}

int change(unsigned int paisa) {
    int coins[6] = {1, 5, 10, 25, 100, 500};
    int mainCoins[6]
    unsigned int thisChange = paisa % 10;
    return thisChange;
}
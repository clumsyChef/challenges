let mainArr = [1, 2, 2, 3, 1, 6, 7, 8, 5, 4, 9, 9, 9];

let finalArr = mainArr.reduce((prev, next) => {
    if(prev.indexOf(next) === -1) {
        prev.push(next)
    }
    return prev;
}, [])

console.log(finalArr)

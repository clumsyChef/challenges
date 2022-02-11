// MAKING CHANGE
// https://www.reddit.com/r/dailyprogrammer/comments/nucsik/20210607_challenge_393_easy_making_change/

const change = (paisa) => {
	let paisaNow = paisa;
	let totalCoins = 0;
	const coins = [1, 5, 10, 25, 100, 500].filter((coin) => coin < paisa).reverse();

	coins.forEach((coin) => {
		let remaining = paisaNow % coin;
		let divi = paisaNow - remaining;
		paisaNow = remaining;
		let thisCoinsTotal = divi / coin;
		totalCoins += thisCoinsTotal;
	});

	return totalCoins;
};

change(0);
change(12);
change(468);
change(123456);

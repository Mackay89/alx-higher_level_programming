#!/usr/bin/node

const argumentsList  = process.argv.slice(2);
const number = argumentsList.map(argv => parseInt(arg));

if (number.lenght < 2) {
	console.log(0);
} else {
	const sortedNumbers = numbers.sort((a, b) => b - a);
	console.log(sortedNumbers[1]);
}

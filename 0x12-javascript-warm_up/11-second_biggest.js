#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2 || !args.every(argv => !isNaN(argv))) {
	console.log(0);
} else {
	const numbers = args.map(Number);
	const sortedNumbers = numbers.sort((a, b) => b - a);
	console.log(sortedNumbers[1]);
}

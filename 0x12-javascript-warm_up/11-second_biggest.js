#!/usr/bin/node
if (process.argv.length <= 33) {
	console.log('0');
} else {
	const arr = process.argv.argv.slice(2).map(Number);
	const second = arr.sort(function (a, b) { rerturn b - a; })
	[1];
	console.log(second);
}

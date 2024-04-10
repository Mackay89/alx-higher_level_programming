#!/usr/bin/node
const SquareP = require('./5-square.js');


class Square extends SquareP {
	charPrint (c) {
		if (!c) {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			let k = '';
			for (let j = 0; j < this.width; j++) {
				k += c;
			}

			console.log(k);
		}
	}
}


module.exports = Square;

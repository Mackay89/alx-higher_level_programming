#!/usr/bin/node


class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		} else {
			this.width = 0;
			this.height = 0;
		}
	}


	print() {
		if (this.width === 0 || this.height === 0) {
			return;
		}


		for (let i = 0; i < this.height; i++) {
			let k = '';
			for (let j = 0; j < this.width; j++) {
				k += 'X';
			}
			console.log(k);
		}
	}
}


module.eports = Rectangle;

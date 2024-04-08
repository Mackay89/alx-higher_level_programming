#!/usr/bin/node
const myObject = {
	type: 'object',
	valuew: 12
};
console.log(myObject);
myObject.incr = function () {
	this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

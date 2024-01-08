#!/usr/bin/node
let num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : 'My number: ' + num);

#!/usr/bin/node
const size = process.argv.length;
console.log(size === 2 ? 'No argument' : size === 3 ? 'Argument found' : 'Arguments found');

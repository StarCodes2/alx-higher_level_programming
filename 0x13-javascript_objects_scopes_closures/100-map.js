#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((num, index) => num * index);
console.log(newList);

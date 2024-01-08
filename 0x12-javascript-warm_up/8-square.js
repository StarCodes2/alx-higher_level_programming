#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
let i;
let line = '';
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    line = line + 'X';
  }
  for (i = 0; i < size; i++) {
    console.log(line);
  }
}

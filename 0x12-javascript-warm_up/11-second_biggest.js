#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numArr = process.argv.map(Number).slice(2, process.argv.length)
    .sort((a, b) => b - a);
  console.log(numArr[1]);
}

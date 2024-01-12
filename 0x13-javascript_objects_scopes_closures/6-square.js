#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      const line = c.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(line);
      }
    }
  }
};

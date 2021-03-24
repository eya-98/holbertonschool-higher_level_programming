#!/usr/bin/node
const X = require('./5-square');
module.exports = class Square extends X {
  charPrint (c) {
    let i, j;
    let line = '';
    if (c === undefined) {
      return this.print;
    } else {
      for (i = 0; i < this.width; i++) {
        line += 'C';
      }
    }
    for (j = 0; j < this.height; j++) {
      console.log(line);
    }
  }
};

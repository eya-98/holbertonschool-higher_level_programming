#!/usr/bin/node
const X = require('./5-square');
module.exports = class Square extends X {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i, j;
    let line = '';
    for (i = 0; i < this.width; i++) {
      if (c === undefined) {
        line += 'X';
      } else {
        line += 'C';
      }
    }
    for (j = 0; j < this.height; j++) {
      console.log(line);
    }
  }
};

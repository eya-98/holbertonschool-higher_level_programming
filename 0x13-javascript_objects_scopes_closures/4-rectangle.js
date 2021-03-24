#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;
    let line = '';
    for (i = 0; i < this.width; i++) {
      line += 'X';
    }
    for (j = 0; j < this.height; j++) {
      console.log(line);
    }
  }

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  double () {
    this.width = this.width * 2;
    this.height *= 2;
  }
};

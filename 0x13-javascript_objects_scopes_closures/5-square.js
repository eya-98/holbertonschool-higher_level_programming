#!/usr/bin/node
const X = require('./4-rectangle');
module.exports = class Square extends X {
  constructor (size) {
    super(size, size);
  }
};

#!/usr/bin/node
const X = require('./4-rectangle');
module.exports = class Rectangle extends X {
  constructor (size) {
    super(size, size);
  }
};

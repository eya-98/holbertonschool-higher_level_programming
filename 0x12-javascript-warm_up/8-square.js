#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (isNaN(Number(argv[2])) === true) {
  console.log('Missing size');
} else {
  for (let height = 0; height < argv[2]; height++) {
    let string = '';
    for (let width = 0; width < argv[2]; width++) {
      string += 'X';
      if (width === argv[2] - 1) {
        console.log(string);
      }
    }
  }
}

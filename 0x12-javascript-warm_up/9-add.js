#!/usr/bin/node
const process = require('process');
const argv = process.argv;
function add (a, b) {
  if (isNaN(Number(a)) === false && isNaN(Number(b)) === false) {
    console.log(Number(a) + Number(b));
  } else {
    console.log(NaN);
  }
}
add(argv[2], argv[3]);

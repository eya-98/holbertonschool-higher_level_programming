#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (isNaN(Number(argv[2])) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}

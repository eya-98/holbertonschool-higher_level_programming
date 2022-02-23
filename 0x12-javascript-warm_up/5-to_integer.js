#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (argv.length === 3) {
  if (isNaN(Number(argv[2])) === false) {
    console.log('My number: ' + argv[2]);
  } else {
    console.log('Not a number');
  }
}

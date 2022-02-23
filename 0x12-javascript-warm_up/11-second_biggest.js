#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (argv.length < 4) {
  console.log(0);
} else {
  let bigger = 0;
  let secondB = 0;
  for (let i = 2; i < argv.length; i++) {
    if (bigger < argv[i]) {
      bigger = argv[i];
    }
  }
  for (let i = 2; i < argv.length; i++) {
    if (secondB < argv[i]) {
      if (argv[i] !== bigger) {
        secondB = argv[i];
      }
    }
  }
  console.log(secondB);
}

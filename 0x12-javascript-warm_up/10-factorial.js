#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const num = argv[2];
if (isNaN(Number(num)) === true) {
  console.log(1);
} else {
  const factorielnum = 1;
  console.log(factoriel(num, factorielnum));
}
function factoriel (num, factorielnum) {
  const number = Number(num);
  if (number === 1) {
    return factorielnum;
  } else {
    factorielnum *= number;
    return factoriel(number - 1, factorielnum);
  }
}

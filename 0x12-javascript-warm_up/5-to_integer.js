#!/usr/bin/node
const var1 = process.argv[2];
if (isNaN(var1) === true) {
  console.log('Not a number');
} else {
  console.log(var1);
}

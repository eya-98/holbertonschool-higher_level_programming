#!/usr/bin/node
let var1 = 0;
process.argv.forEach((val, index) => {
  var1++;
  if (var1 === 3) {
    console.log(process.argv[2] + ' is ' + process.argv[3]);
  }
});
if (var1 < 3) {
  console.log('No argument');
}

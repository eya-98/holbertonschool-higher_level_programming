#!/usr/bin/node
let var1 = 0;
process.argv.forEach((val, index) => {
  var1++;
  if (var1 === 3) {
    console.log(`${val}`);
  }
});
if (var1 < 3) {
  console.log('No argument');
}

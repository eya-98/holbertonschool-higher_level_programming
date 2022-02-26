#!/usr/bin/node
const process = require('process');
const file = process.argv[2];
const content = process.argv[3];
const fs = require('fs');
fs.writeFile(file, content, 'utf-8', bar);
function bar (err) {
  if (err) {
    console.log(err);
  }
}

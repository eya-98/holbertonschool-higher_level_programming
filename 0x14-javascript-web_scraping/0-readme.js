#!/usr/bin/node
const process = require('process');
const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', bar);
function bar (err, data) {
  err ? console.log(err) : console.log(data);
}

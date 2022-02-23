#!/usr/bin/node
const process = require('process');
argv = process.argv
console.log(argv[2])
if (argv.length === 3) {
    console.log(argv[2])
    if (isNaN(Number(argv[2])) == false) {
        console.log(argv[2] + ": <first argument converted in integer>")
     }
     else {
         console.log('Not a number')
     }
 }
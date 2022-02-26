#!/usr/bin/node
const process = require('process');
const url = 'https://swapi-api.hbtn.io/api/films/:id';
const id = process.argv[2];
console.log(id);
const theUrl = url.replace(':id', id);
const request = require('request');
request.get(theUrl, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    const body = JSON.parse(response.body);
    console.log(body.title);
  }
});

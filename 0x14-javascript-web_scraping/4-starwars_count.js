#!/usr/bin/node
const character = 'https://swapi-api.hbtn.io/api/people/18/';
const request = require('request');
request.get(character, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    const body = JSON.parse(response.body);
    console.log(body.films.length);
  }
});

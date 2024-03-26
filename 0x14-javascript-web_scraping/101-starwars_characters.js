#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function printInOrder (characters, index) {
  request(characters[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (characters.length > index + 1) {
        printInOrder(characters, index + 1);
      }
    }
  });
}

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printInOrder(characters, 0);
  }
});

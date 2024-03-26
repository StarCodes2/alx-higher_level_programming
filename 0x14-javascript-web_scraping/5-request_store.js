#!/usr/bin/node
const request = require('request');
const f = require('fs');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    f.writeFile(process.argv[3], body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});

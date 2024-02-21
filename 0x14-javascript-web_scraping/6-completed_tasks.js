#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const complete = {};
    const todos = JSON.parse(body);
    todos.forEach((todo) => {
      if (todo.completed && complete[todo.userId] === undefined) {
        complete[todo.userId] = 1;
      } else if (todo.completed) {
        complete[todo.userId] += 1;
      }
    });
    console.log(complete);
  }
});

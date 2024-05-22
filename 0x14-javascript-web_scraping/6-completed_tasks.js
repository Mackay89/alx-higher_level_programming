#!/usr/bin/node


const request = require('request');


request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);


    for (let j = 0; j < body.length; ++j) {
      const userId = body[j].userId;
      const completed = body[j].completed;


      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }


      if (completed) ++completedTasksUsers[userId];
    }


    console.log(completedTasksByUsers);
  }
});
	    

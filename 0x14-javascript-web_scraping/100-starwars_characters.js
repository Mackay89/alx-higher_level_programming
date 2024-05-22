#!/usr/bin/node


const request = require('request');
const starWarsUri = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);


request(starWarsUri, function (error, response, body) {
  const characters = JSON.parse(body).characters;


  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (cErr, cResponse, cbody) {
      console.log(JSON.parse(cbody).name);
    });
  }
});

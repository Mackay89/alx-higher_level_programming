#!/usr/bin/node


const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;


request(starWarsUri, function (error, response, body) {
  body = JSON.parse(body).results;


  for (let i = 0; i < body.length; ++i) {
  const characters = body[i].characters;


  for (let k = 0; k < characters.length; ++k) {
    const character = characters[k];
    const characterId = character.split('/')[5];


    if (characterId === '18') {
      times += 1;
    }
  }
  }


  console.log(times);
});

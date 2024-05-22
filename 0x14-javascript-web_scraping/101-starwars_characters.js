#!/usr/bin/node


const request = require('request');


const movieId = process.argv[2];
const apiUrl = 'https://swapi.dev/api/films/${movieId}/';


request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }


  if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode)
    return;
  }


  const film = JSON.parse(body);
  const charactersUrls = film.characters;


  const	 getCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, function (error, response, body) {
        if (error) {
          reject(error);
	} else {
	  const character = JSON.parse(body);
          resolve(character.name);
	}
      });
    });
  };


  Promise.all(charactersUrls.map(getCharacterName))
    .then((characters) => {
      characters.forEach((character) => {
        console.log(character);
      });
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});

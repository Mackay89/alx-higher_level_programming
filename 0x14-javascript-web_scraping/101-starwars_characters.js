#!/usr/bin/node


const request = require('request')


const movieId = process.argv[2];
const base_Url = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = base_Url.concat(movieId);


request(fullUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const characterPromises = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (!error && response.statusCode === 200) {
	    const characterData = JSON.parse(body).name;
            resolve(characterData);
	  } else {
	    reject(new Error ('Failed to fetch character data'));
	  }
	});
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      console.log(characterNames.join('\n'));
      })
      .catch(error => {
        console.error(error.message);
      });
  } else {
    console.error(error || 'Failed to fetch movie data', error);
  }
});

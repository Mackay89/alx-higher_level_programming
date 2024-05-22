#!/usr/bin/node


const request = require('request');


function getDataFrom(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, resp, body) => {
       if (error) {
	 reject(error);
	} else {
	  resolve(body);
	}
    });
  });
}


function errorHandler(error) {
  console.error(error);
}


async function printMovieCharacters(movieId) {
  try {
    const movieUri = 'https://swapi.dev/api/films/${movieId}';
    const movieData = await getDataFrom(movieUri);
    console.log("Movie Data:", movieData);
    const movie = JSON.parse(movieData);
    console.log("Movie:", movie);
    const characters = movie.characters;
    console.log("Character:", characters);


    const promise = characters.map(characterUrl => getDataFrom(characterUrl));
    const characterResponses = await Promise.all(promises);


    for (const characterResponse of characterResponses) {
      const character = JSON.parse(characterResponse);
      console.log(character.name);
    }
  } catch (error) {
    errorHandler(error);
  }
}


  const movieId = process.argv[2];
  if (!movieId) {
    console.error("Please provide a movie ID.");
  } else {
    printMovieCharacters(movieId)
  }


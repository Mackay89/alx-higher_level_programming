#!/usr/bin/node


const request = require('request');
const util = require('util');


const get = util.promisify(request.get);


get(process.argv[2])
  .then(response => {
    console.log('Status code: ${response.status}');
  })
  .catch(error => {
    console.error(error);
  });

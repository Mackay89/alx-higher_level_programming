#!/usr/bin/node


const fs = require('fs')

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Use fs.readFile() to read the contents of a file specified as a command-line argument
  // 'utf8' specified the encoding of the file being  read

   if (error) {
     // If an error occcurs the file read the operation, the 'error' parameter will contain an error object.
     console.error('Error reading the file:', error);
   } else {
     console.log(content);
   }
});

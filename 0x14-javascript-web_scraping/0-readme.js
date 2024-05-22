#!/usr/bin/node


const fs = require('fs')

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}


const filePath = process.argv[2];


fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    if (err.code === 'ENOENT') {
      console.error(`Error: File '${filePath}' does not exist.`);
    } else {
      console.error('Error reading file: ${err.message}');
    }
    process.exit(1);
  } else {
    process.stdout.write(data);
  }
});

#!/usr/bin/node
const f = require('fs');
const file1 = f.readFileSync(process.argv[2], 'utf8');
const file2 = f.readFileSync(process.argv[3], 'utf8');
f.writeFileSync(process.argv[4], file1 + file2);

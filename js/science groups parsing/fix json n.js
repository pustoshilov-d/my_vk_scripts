// groups science.json

import { readFileSync } from 'fs';

let obj = JSON.parse(readFileSync('groups science.json'));
console.log(obj.mykey)
#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square extends Square {
  charPrint (c) {
    const char = c || undefined;
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};

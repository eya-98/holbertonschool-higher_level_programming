#!/usr/bin/node
exports.esrever = function (list) {
    let i = 0;
    let j = 0;
    let k = 0;
    const p = [];
    for (i = 0; list[i]; i++) {
    }
    for (j = i - 1; j >= 0; j--) {
      p[k] = list[j];
      k++;
    }
    return p;
  };
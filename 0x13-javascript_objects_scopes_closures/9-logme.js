#!/usr/bin/node
let callcount = -1;
exports.logMe = function (item) {
  callcount += 1;
  console.log(callcount + ':', item);
};

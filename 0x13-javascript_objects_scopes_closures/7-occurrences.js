#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbre = 0;
  for (const i in list) {
    if (searchElement === list[i]) {
      nbre += 1;
    }
  }
  return nbre;
};

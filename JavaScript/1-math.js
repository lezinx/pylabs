'use strict'

const prompt = require('prompt');

prompt.start()

prompt.get([
  'x', // any number between -2.4 < x < 2.4
  'epsilon' // accuracy
], function (err, result) {
  let res = cal(result.x, result.epsilon);
  console.log(res);
});


function cal(x, epsilon) {
  if (x >= 2.4 || x <= -2.4) throw new Error('x must be in range (-2.4; 2.4)');
  let fn1 = (x) => (Math.pow(Math.E, x) * (parseInt(x) + 1));
  let fn = fn1(x);
  let count, res = 0;
  for (let n = 0; fn - res > epsilon; n++) {
    res = res + Math.pow(x, n) * (n + 1) / (factorial(n));
    count = n;
  }
  console.log(res);
  return (count) || 0;
}

function factorial(x) {
  if (x > 0) return x * factorial(x - 1);
  else if (x === 0) return 1;
  else return -1;
}

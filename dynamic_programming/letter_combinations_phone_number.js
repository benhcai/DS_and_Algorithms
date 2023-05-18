/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
  if (digits === "") return [];
  const digArr = parseDigs(digits);
  const combs = createCombos(digArr);

  const ans = [];
  const recur = (arr, curr, pos) => {
    if (curr.length === combs.length - 1) {
      for (const el of combs[combs.length - 1]) {
        const res = [...curr, el];
        ans.push(res.join(""));
      }
      return;
    }
    for (let i = 0; i < arr.length; i++) {
      curr.push(arr[i]);
      recur(combs[pos + 1], curr, pos + 1);
      curr.pop();
    }
  };
  recur(combs[0], [], 0);

  return ans;
};

function parseDigs(digits) {
  const stack = [];
  for (let i = 0; i < digits.length; i++) {
    stack.push(parseInt(digits[i]));
  }
  return stack;
}

function createCombos(digArr) {
  const map = {
    1: [],
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  };

  const combs = [];
  for (const el of digArr) {
    combs.push(map[el]);
  }
  return combs;
}

const ans = letterCombinations("23");
console.log(ans);

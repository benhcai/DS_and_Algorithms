/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  // seenMatrix
  const seenMatrix = [];
  for (const row of board) {
    const r = [];
    for (const _ of row) {
      r.push(0);
    }
    seenMatrix.push(r);
  }

  // matrix traversal
  // up
  // down
  // left
  // right
  const traverse = (i, j, letterId) => {
    const found = letterId === word.length;
    if (found) return true;
    const outBounds = i < 0 || i === board.length || j < 0 || j === board[0].length;
    if (outBounds) return false;
    const isSeen = seenMatrix[i][j] === 1;
    const wrongLetter = word[letterId] !== board[i][j];
    if (isSeen || wrongLetter) return false;
    seenMatrix[i][j] = 1;
    // recurse in directions
    if (traverse(i, j - 1, letterId + 1)) return true;
    if (traverse(i, j + 1, letterId + 1)) return true;
    if (traverse(i - 1, j, letterId + 1)) return true;
    if (traverse(i + 1, j, letterId + 1)) return true;
    // unmark matrix
    seenMatrix[i][j] = 0;
  };

  // loop through x
  // loop through y
  // traverse(x,y)
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (traverse(i, j, 0)) return true;
    }
  }
  return false;
};

const board = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"],
];
const word = "ABCzED";

console.log(exist(board, word));

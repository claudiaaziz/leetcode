/**
 * Hash Map - Matrix
 * Time O(ROWS * COLS) | Space O(ROWS * COLS)
 * https://leetcode.com/problems/valid-sudoku/
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = (board) => {
  const boards = 3;
  const [boxes, cols, rows] =
    getBoards(boards); /* Time O(ROWS * COLS) | Space O(ROWS * COLS) */

  return searchGrid(
    board,
    boxes,
    cols,
    rows
  ); /* Time O(ROWS * COLS) | Space O(ROWS * COLS) */
};

var initBoard = (rows, cols) =>
  new Array(rows).fill().map(() => new Array(cols).fill(false));

var getBoards = (boards) => {
  const [rows, cols] = [9, 9];

  return new Array(boards).fill().map(() => initBoard(rows, cols));
};

var searchGrid = (board, boxes, cols, rows) => {
  const [_rows, _cols] = [9, 9];

  for (let row = 0; row < _rows; row++) {
    /* Time O(ROWS)*/
    for (let col = 0; col < _cols; col++) {
      /* Time O(COLS)*/
      const char = board[row][col];
      const index = Math.floor(row / 3) * 3 + Math.floor(col / 3);

      const isEmpty = char === '.';
      if (isEmpty) continue;

      const hasMoved =
        boxes[index][char - 1] || cols[col][char - 1] || rows[row][char - 1];
      if (hasMoved) return false;

      rows[row][char - 1] = true; /* Space O(ROWS * COLS)*/
      cols[col][char - 1] = true; /* Space O(ROWS * COLS)*/
      boxes[index][char - 1] = true; /* Space O(ROWS * COLS)*/
    }
  }

  return true;
};

/**
 * Array - Fixed Size
 * Time O(ROWS * COLS) | Space O(CELLS)
 * https://leetcode.com/problems/valid-sudoku/
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = (board) => {
  const [boards, cells] = [3, 9];
  const [boxes, rows, cols] = getBoards(
    boards,
    cells
  ); /* Time O(ROWS * COLS) | Space O(CELLS) */

  return searchGrid(
    board,
    boxes,
    rows,
    cols
  ); /* Time O(ROWS * COLS) | Space O(CELLS) */
};

var getBoards = (boards, cells) =>
  new Array(boards).fill().map(() => new Array(cells).fill(0));

var searchGrid = (board, boxes, rows, cols) => {
  const [_rows, _cols] = [9, 9];

  for (let row = 0; row < _rows; row++) {
    /* Time O(ROWS)*/
    for (let col = 0; col < _cols; col++) {
      /* Time O(COLS)*/
      const char = board[row][col];
      const position = 1 << (char - 1);
      const index = Math.floor(row / 3) * 3 + Math.floor(col / 3);

      const isEmpty = char === '.';
      if (isEmpty) continue;

      const hasMoved =
        boxes[index] & position || cols[col] & position || rows[row] & position;
      if (hasMoved) return false;

      rows[row] |= position; /* Space O(CELLS)*/
      cols[col] |= position; /* Space O(CELLS)*/
      boxes[index] |= position; /* Space O(CELLS)*/
    }
  }

  return true;
};

//

/**
 * Set-Based Iterative
 * Time O(ROWS + COLS + BOXES) | Space O(1)
// https://leetcode.com/problems/valid-sudoku/solutions/476369/javascript-solution-beats-100-with-explanation-real-explanations/
 */

// The third solution can be referred to as the "Set-Based Iterative" approach for validating a Sudoku board. Here's why:

// Set-Based: This method utilizes three sets (row, col, and box) in each iteration to track the numbers that have already been seen in the respective row, column, and 3x3 box. Sets are a natural choice for this task because they efficiently handle the operations of checking for existence and adding new elements, which are both crucial in this context.

// Iterative: The solution iterates through each cell in the Sudoku board, checking the constraints for Sudoku: each number must appear exactly once in each row, column, and 3x3 box. The iterative process, combined with the use of sets, ensures that each number is validated against the Sudoku rules.

// Time Complexity: The time complexity is O(ROWS * COLS), similar to the first two solutions, as it iterates through each cell of the board once.

// Space Complexity: The space complexity is O(ROWS + COLS + BOXES), but since the size of the Sudoku board is fixed (9x9), this can also be considered O(1) - constant space complexity. Each set is recreated for each row, column, and box, and does not grow larger than the size of the board.

// This solution is different from the first two as it does not preallocate space for tracking all rows, columns, and boxes. Instead, it dynamically creates sets for each row, column, and box during the iteration, which makes it more space-efficient while maintaining the same time efficiency.

var isValidSudoku = function (board) {
  for (let i = 0; i < 9; i++) {
    let row = new Set(),
      col = new Set(),
      box = new Set();

    for (let j = 0; j < 9; j++) {
      let _row = board[i][j];
      let _col = board[j][i];
      let _box =
        board[3 * Math.floor(i / 3) + Math.floor(j / 3)][3 * (i % 3) + (j % 3)];

      if (_row != '.') {
        if (row.has(_row)) return false;
        row.add(_row);
      }
      if (_col != '.') {
        if (col.has(_col)) return false;
        col.add(_col);
      }

      if (_box != '.') {
        if (box.has(_box)) return false;
        box.add(_box);
      }
    }
  }
  return true;
};

// t o(1) - s o(1)
var isValidSudoku = function (board) {
  const seen = new Set();

  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      let currentEle = board[r][c];

      if (currentEle !== '.') {
        const rowStr = `${currentEle} found in row ${r}`;
        const colStr = `${currentEle} found in col ${c}`;
        const squareStr = `${currentEle} found in square ${Math.floor(
          r / 3
        )}-${Math.floor(c / 3)}`;

        if (seen.has(rowStr) || seen.has(colStr) || seen.has(squareStr))
          return false;
        seen.add(rowStr);
        seen.add(colStr);
        seen.add(squareStr);
      }
    }
  }

  return true;
};

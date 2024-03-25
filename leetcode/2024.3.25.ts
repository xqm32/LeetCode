/*
 * @lc app=leetcode.cn id=529 lang=typescript
 *
 * [529] 扫雷游戏
 */

// @lc code=start
function updateBoard(board: string[][], click: number[]): string[][] {
	const [row, col] = click;
	if (board[row][col] === "M") {
		board[row][col] = "X";
	} else {
		dfs(board, row, col);
	}
	return board;
}

function dfs(board: string[][], row: number, col: number) {
	const rows = board.length;
	const cols = board[0].length;
	if (
		row < 0 ||
		row >= rows ||
		col < 0 ||
		col >= cols ||
		board[row][col] !== "E"
	) {
		return;
	}
	const mines = countMines(board, row, col);
	if (mines > 0) {
		board[row][col] = mines.toString();
	} else {
		board[row][col] = "B";
		for (let i = -1; i <= 1; i++) {
			for (let j = -1; j <= 1; j++) {
				dfs(board, row + i, col + j);
			}
		}
	}
}

function countMines(board: string[][], row: number, col: number): number {
	const rows = board.length;
	const cols = board[0].length;
	let count = 0;
	for (let i = -1; i <= 1; i++) {
		for (let j = -1; j <= 1; j++) {
			if (
				row + i >= 0 &&
				row + i < rows &&
				col + j >= 0 &&
				col + j < cols &&
				board[row + i][col + j] === "M"
			) {
				count++;
			}
		}
	}
	return count;
}
// @lc code=end

/*
 * @lc app=leetcode.cn id=640 lang=typescript
 *
 * [640] 求解方程
 */

// @lc code=start
function solveEquation(equation: string): string {
  const [left, right] = equation.split("=");
  const leftX = parse(left);
  const rightX = parse(right);
  const x = leftX[0] - rightX[0];
  const num = rightX[1] - leftX[1];
  if (x === 0) {
    if (num === 0) {
      return "Infinite solutions";
    }
    return "No solution";
  }
  return `x=${num / x}`;
}

function parse(str: string): [number, number] {
  let x = 0;
  let num = 0;
  let flag = 1;
  let temp = "";
  for (let i = 0; i < str.length; i++) {
    if (str[i] === "x") {
      if (temp === "" || temp === "+") {
        x += flag;
      } else if (temp === "-") {
        x -= flag;
      } else {
        x += flag * parseInt(temp);
      }
      temp = "";
    } else if (str[i] === "+" || str[i] === "-") {
      if (temp === "") {
        temp = str[i];
      } else {
        num += flag * parseInt(temp);
        temp = str[i];
      }
    } else {
      temp += str[i];
    }
  }
  if (temp) {
    num += flag * parseInt(temp);
  }
  return [x, num];
}
// @lc code=end

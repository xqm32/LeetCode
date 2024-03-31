/*
 * @lc app=leetcode.cn id=385 lang=typescript
 *
 * [385] 迷你语法分析器
 */

// @lc code=start
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     If value is provided, then it holds a single integer
 *     Otherwise it holds an empty nested list
 *     constructor(value?: number) {
 *         ...
 *     };
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     isInteger(): boolean {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     getInteger(): number | null {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     setInteger(value: number) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     add(elem: NestedInteger) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds,
 *     or an empty list if this NestedInteger holds a single integer
 *     getList(): NestedInteger[] {
 *         ...
 *     };
 * };
 */

function deserialize(s: string): NestedInteger {
	if (s[0] !== "[") {
		return new NestedInteger(+s);
	}
	const stack: NestedInteger[] = [];
	let num = "";
	for (let i = 0; i < s.length; i++) {
		const c = s[i];
		if (c === "[") {
			stack.push(new NestedInteger());
		} else if (c === "]") {
			if (num) {
				stack[stack.length - 1].add(new NestedInteger(+num));
				num = "";
			}
			const top = stack.pop();
			if (stack.length) {
				stack[stack.length - 1].add(top);
			} else {
				return top;
			}
		} else if (c === ",") {
			if (num) {
				stack[stack.length - 1].add(new NestedInteger(+num));
				num = "";
			}
		} else {
			num += c;
		}
	}
	return new NestedInteger();
}
// @lc code=end

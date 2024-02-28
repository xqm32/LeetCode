/*
 * @lc app=leetcode.cn id=310 lang=typescript
 *
 * [310] 最小高度树
 */

// @lc code=start
function findMinHeightTrees(n: number, edges: number[][]): number[] {
  if (n === 1) return [0];

  const graph: number[][] = Array.from({ length: n }, () => []);
  const degree: number[] = Array.from({ length: n }, () => 0);

  for (let [a, b] of edges) {
    graph[a].push(b);
    graph[b].push(a);
    degree[a]++;
    degree[b]++;
  }

  const queue: number[] = [];
  for (let i = 0; i < n; i++) {
    if (degree[i] === 1) {
      queue.push(i);
    }
  }

  while (n > 2) {
    const size = queue.length;
    n -= size;
    for (let i = 0; i < size; i++) {
      const node = queue.shift()!;
      for (let neighbor of graph[node]) {
        degree[neighbor]--;
        if (degree[neighbor] === 1) {
          queue.push(neighbor);
        }
      }
    }
  }

  return queue;
}
// @lc code=end

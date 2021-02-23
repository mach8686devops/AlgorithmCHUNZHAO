from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        root = {}
        for w in words:
            p = root
            for c in w:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['finish'] = w

        def dfs(start, p):
            i, j = start[0], start[1]
            c = board[i][j]

            last = p[c].pop('finish', False)
            if last:
                res.append(last)

            board[i][j] = '#'
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in p[c]:
                    dfs((ni, nj), p[c])
            board[i][j] = c

            if not p[c]:
                p.pop(c)

        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs((i, j), root)
        return res

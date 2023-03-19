import sys

sys.setrecursionlimit((int(2e5)))

n, x = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
print(g)


def solve():
    ret = 0

    def dfs(cnt, pre):
        ans = 1
        for nxt in g[cnt]:
            if nxt == pre:
                continue
            if (cnt & 1) == (nxt & 1):
                ans += dfs(nxt, cnt)
            else:
                dfs(nxt, cnt)
        nonlocal ret
        ret += ans
        return ans

    dfs(x, -1)
    return ret


print(solve())

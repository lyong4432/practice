import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for i in range(n):
    a, b = map(str, input().split())
    dic[a] = b

for i in range(m):
    k = input().strip()
    print(dic[k])

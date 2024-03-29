import sys

V, E = map(int,sys.stdin.readline().split())

edges = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((A, B, C))

edges.sort(key=lambda abc: abc[2]) # edges = [(1,2,1), (2,3,2), (1,3,3)]

# union - Find
parent = [i for i in range(V+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    else :
        return get_parent(parent[x])

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

def same_parent(a,b):
    return get_parent(a) == get_parent(b)

answer = 0
for a,b,cost in edges:
    if not same_parent(a,b):
        union_parent(a,b)
        answer += cost
print(answer)
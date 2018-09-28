from collections import defaultdict
import random

visited = [False]*2001

def DFS(graph, start):
    if visited[start]: return
    visited[start] = True
    for neig in graph[start]:
        DFS(graph, neig)
    
def SCC(graph, reversed_graph, n_inter):
    initial_node = random.randint(1,n_inter)
    global visited
    visited = [False]*2001
    DFS(graph, 1)
    for i in visited[1:n_inter+1]:
        if not i: return 0
    visited = [False]*2001
    DFS(reversed_graph, 1)
    for i in visited[1:n_inter+1]:
        if not i: return 0
    return 1


def input2():
    value = input()
    while(value == ' ' or value == '' or value == '\n'):
        value = input()
    values = value.split(' ')
    out = []
    for i, v in enumerate(values):
        yield(int(v))

n_inter, n_calles = input2()
while(n_inter + n_calles):
    graph = defaultdict(list)
    reversed_graph = defaultdict(list)
    for i in range(n_inter):
        graph[i+1] = []
        reversed_graph[i+1] = []
    for calle in range(n_calles):
        a, b, tipo = input2()
        if int(tipo) == 1:
            graph[a].append(b)
            reversed_graph[b].append(a)
        if int(tipo) == 2:
            graph[a].append(b)
            graph[b].append(a)
            reversed_graph[a].append(b)
            reversed_graph[b].append(a)
    print(SCC(graph, reversed_graph, n_inter))
    n_inter, n_calles = input2()

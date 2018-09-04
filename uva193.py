from collections import defaultdict
import sys

max = 0
output = 0

def BT(state):
    if -1 in state:
        node = state.index(-1)
        for color in [False, True]:
            state[node] = color
            
            if color == False:
                if [n for n in graph[node+1] if state[n-1] == False]:
                    continue
            BT(state)
            state[node] = -1
    else:
        global max
        global output
        n_black = state.count(False)
        if n_black >= max:
            max = n_black
            output = [i+1 for i, e in enumerate(state) if e == False]
def input2():
    value = input()
    while(value == ' ' or value == '' or value == '\n'):
        value = input()
    return value
    
n_graph = int(input2())
for g in range(n_graph):
    max = 0
    output = 0
    graph = defaultdict(list)
    
    n_nodes, n_edges = input2().split(" ")
    n_nodes = int(n_nodes)
    n_edges = int(n_edges)
    for i in range(n_nodes):
        graph[i+1] = []
    for e in range(n_edges):
        a = input2().split(" ")
        graph[int(a[0])].append(int(a[1]))
        graph[int(a[1])].append(int(a[0]))
    
    state = [-1]*(len(graph))
    BT(state)
    print(len(output))
    printout = ' '.join([str(v) for v in output])
    print(printout)
exit(0)
    

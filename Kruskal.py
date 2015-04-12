'''
Kruskal's Algorith for the MST.
Union find searches for cycles
11 4 2013 
'''
import queue

q=queue.PriorityQueue()
parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice], rank[vertice] = vertice, 0
    

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    root1, root2= find(vertice1), find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1


def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    
    for edge in list(graph['edges']): q.put(edge)
    edges=[q.get() for edge in range(len(list(graph['edges'])))]

    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree


graph = {'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
         'edges': set([(1, 'A', 'B'),(5, 'A', 'C'),
                       (3, 'A', 'D'),(4, 'B', 'C'),
                       (2, 'B', 'D'),(1, 'C', 'D'),
                     ])}

print(kruskal(graph))
'''
minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
assert kruskal(graph) == minimum_spanning_tree
'''

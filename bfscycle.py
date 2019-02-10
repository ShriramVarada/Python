import collections

"""
Problem 3, Homework 2
"""


def bfs(G, s):
    """
    >>> G = {'a': ['c'], 'b': ['c'], 'c': ['a', 'b', 'd', 'e'], 'd': ['c', 'e'], 'e': ['c', 'd']}
    >>> print(bfs(G, 'c'))
    ['e', 'd', 'c']
    >>> G = {'a': ['c'], 'b': ['c'], 'c': ['a', 'b', 'd', 'e'], 'd': ['c'], 'e': ['c']}
    >>> print(bfs(G, 'c'))
    []
    """

    q = collections.deque()
    q.append(s)
    discovered = {}
    parent = {}
    layer = 1
    layernode = {layer: []}
    for n in G.keys():
        discovered[n] = False
        parent[n] = True
    discovered[s] = True
    layernode[layer].append(s)
    layer += 1
    while q:
        numberofNodesinLayer = len(q)
        while numberofNodesinLayer > 0:
            u = q.popleft()
            for v in G[u]:
                if not discovered[v]:
                    q.append(v)
                    parent[v] = u
                    if layer in layernode:
                        layernode[layer].append(v)
                    else:
                        layernode[layer] = [v]
                    discovered[v] = True
            numberofNodesinLayer -= 1
        if numberofNodesinLayer == 0:
            layer += 1
    layer -= 1
    i = 2
    node1 = None
    node2 = None
    notAdjedge = True
    while notAdjedge and i < layer:
        listlayer = layernode[i]
        for j in range(len(listlayer)):
            for k in range(j+1, len(listlayer)):
                if listlayer[k] in G[listlayer[j]]:
                    notAdjedge = False
                    node1 = listlayer[k]
                    node2 = listlayer[j]
                    break
            if not notAdjedge:
                break
        i += 1

    if node1 is None and node2 is None:
        return []

    cycle = [node1, node2]

    while parent[node1] != parent[node2]:
        cycle.append(parent[node1])
        cycle.append(parent[node2])
        node1 = parent[node1]
        node2 = parent[node2]

    node1 = parent[node1]
    cycle.append(node1)

    return cycle


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
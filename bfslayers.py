import collections

"""
Problem 1, Homework 2

Run this program as main.
Uses doctest to validate the answer as a dictionary which maps the layer number
to the nodes that are present in it.
Pass to the bfs function, the graph in the form of a dictionary and a starting node
"""


def bfs(G, s):

    """
    >>> G = {1: [2, 3], 2: [1, 3, 5, 4], 3: [1, 2, 5, 7, 8], 4: [2, 5], 5: [2, 3, 4, 6], 6: {5}, 7: {3, 8}, 8: {3, 7}}
    >>> print(bfs(G, 1))
    {1: [1], 2: [2, 3], 3: [5, 4, 7, 8], 4: [6]}
    """

    q = collections.deque()
    q.append(s)
    discovered = {}
    parent = {}
    layer = 1
    layernode = {1: []}
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
    return layernode


if __name__== "__main__":
    import doctest
    doctest.testmod(verbose=True)

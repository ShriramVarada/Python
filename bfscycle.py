import collections
import importlib
"""
Problem 3, Homework 2
"""


def bfs(G, s):
    """
    >>> G = {'a': ['c'], 'b': ['c'], 'c': ['a', 'b', 'd', 'e'], 'd': ['c', 'e'], 'e': ['c', 'd']}
    >>> print(bfs(G, 'c'))
    ['d', 'e', 'c']
    >>> G = {'a': ['c'], 'b': ['c'], 'c': ['a', 'b', 'd', 'e'], 'd': ['c'], 'e': ['c']}
    >>> print(bfs(G, 'c'))
    []
    """

    q = collections.deque()
    q.append(s)
    discovered = {}
    parent = {}
    T = {s: []}
    for n in G.keys():
        discovered[n] = False
        parent[n] = True
    discovered[s] = True
    while q:
            u = q.popleft()
            for v in G[u]:
                if not discovered[v]:
                    q.append(v)
                    parent[v] = u
                    if u in T:
                        T[u].append(v)
                    else:
                        T[u] = [v]
                    discovered[v] = True

    leftedges = dict(G)

    for node, conn in T.items():
        for x in conn:
            leftedges[node].remove(x)
            leftedges[x].remove(node)

    node1 = None
    node2 = None

    for node, conn in leftedges.items():
        if conn:
            node1 = node
            node2 = conn[0]
            break

    if not node1 and not node2:
        return []
    else:
        cycle = [node1, node2]
        hasedge = False
        while parent[node1] != parent[node2]:
            node1 = parent[node1]
            node2 = parent[node2]
            if node1 in G[node2]:
                hasedge = True
                cycle.append(node1)
                cycle.append(node2)
                break
            cycle.append(node1)
            cycle.append(node2)

    if hasedge:
        return cycle
    else:
        cycle.append(parent[node1])
        return cycle
    # c = list(edges.keys())[0]
    # d = edges[c][0]
    #
    # hasedge = False
    # cycle = []
    # while not hasedge:
    #     cycle.append(c)
    #     cycle.append(d)
    #     c = parent[c]
    #     d = parent[d]
    #     if c is d:
    #         cycle.append(c)
    #         return cycle
    #     elif c in G2[d] or d in G2[c]:
    #         hasedge = True
    #         cycle.append(c)
    #         cycle.append(d)
    #
    # if not hasedge:
    #     return []
    # else:
    #     return cycle



    # i = 2
    # node1 = None
    # node2 = None
    # notAdjedge = True
    # while notAdjedge and i < layer:
    #     listlayer = layernode[i]
    #     for j in range(len(listlayer)):
    #         for k in range(j+1, len(listlayer)):
    #             if listlayer[k] in G[listlayer[j]]:
    #                 notAdjedge = False
    #                 node1 = listlayer[k]
    #                 node2 = listlayer[j]
    #                 break
    #         if not notAdjedge:
    #             break
    #     i += 1
    #
    # if node1 is None and node2 is None:
    #     return []
    #
    # cycle = [node1, node2]
    #
    # while parent[node1] != parent[node2]:
    #     cycle.append(parent[node1])
    #     cycle.append(parent[node2])
    #     node1 = parent[node1]
    #     node2 = parent[node2]
    #
    # node1 = parent[node1]
    # cycle.append(node1)



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
from __future__ import print_function  # to allow Python 2 to use print function


def parent(i): return (i - 1) // 2


def leftChild(i): return 2 * i + 1


def rightChild(i): return 2 * i + 2


def heapifyUp(H, i):
    """ Given heap H, perform the heapifyUp operation
        on the element at position i (i.e., continues to
        swap element with parent if element is smaller)
    """
    if i > 0:
        j = parent(i)
        if H[i] < H[j]:
            H[i], H[j] = H[j], H[i]
            heapifyUp(H, j)


def heapifyDown(H, i):
    """ Given heap H, perform the heapifyDown operation
        on the element at position i (i.e., continues to
        swap element with smaller child if element is
        larger)
    """
    n = len(H)
    if leftChild(i) >= n:
        return
    # j will be the index of the smaller child
    j = leftChild(i)
    if j < n - 1:  # there exists a right child
        if H[rightChild(i)] < H[j]:
            j = rightChild(i)
    if H[j] < H[i]:
        H[i], H[j] = H[j], H[i]
        heapifyDown(H, j)


class PriorityQueue3:
    """ PriorityQueue3 provides an implementation of a
        priority queue using heaps with the following methods:
            -insert(item,key)
            -findMin()
            -delete(item)
            -extractMin()
            -changeKey(item,newKey)

    Example usage:
    >>> Q = PriorityQueue3()
    >>> Q.insert('a',5)
    >>> Q.insert('c',2)
    >>> Q.insert('d',7)
    >>> Q.insert('e',4)
    >>> print(Q.findMin())
    c
    >>> Q.delete('e')
    >>> Q.changeKey('c',10)
    >>> print(Q.extractMin())
    a
    >>> print(Q.extractMin())
    d
    >>> print(Q.extractMin())
    c
    """

    def __init__(self):
        """ initializes empty priority queue
        """
        self.dictionary = {}
        self.queue = []

    def insert(self, item, key):
        """ inserts item into the priority queue with given key
        """
        self.queue.append(key)
        self.dictionary[key] = item
        heapifyUp(self.queue, len(self.queue) - 1)

    def findMin(self):
        """ returns the minimum element (but does not delete it)
        """
        return self.dictionary[self.queue[0]]

    def delete(self, item):
        """ deletes item from the priority queue
        """
        key = self.dictionary.keys()[self.dictionary.values().index(item)]
        ind = self.queue.index(key)
        self.queue[ind], self.queue[len(self.queue) - 1] = self.queue[len(self.queue) - 1], self.queue[ind]
        del self.queue[len(self.queue) - 1]
        del self.dictionary[key]
        heapifyUp(self.queue, ind)
        heapifyDown(self.queue, ind)

    def extractMin(self):
        """ deletes and returns item with smallest value
        """
        self.queue[0], self.queue[len(self.queue) - 1] = self.queue[len(self.queue) - 1], self.queue[0]

        x = self.queue.pop()

        heapifyDown(self.queue, 0)

        return self.dictionary[x]

    def changeKey(self, item, newKey):
        """ changes the value of item in the priority queue to newKey
        """
        x = self.dictionary.keys()[self.dictionary.values().index(item)]
        self.queue[self.queue.index(x)] = newKey
        if x > newKey:
            heapifyUp(self.queue, self.queue.index(newKey))
        elif x <= newKey:
            heapifyDown(self.queue, self.queue.index(newKey))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

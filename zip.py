from asyncore import write
from operator import add
import numpy
import queue
from bitarray import bitarray
from tree import TreeNode

def zip(sourcepath):
    pq = queue.PriorityQueue()
    q = queue.Queue()
    char_tracker = {}
    address_tracker = {}

    f = open('./' + sourcepath, 'r')
    for line in f:
        for n in line:
            char_tracker[n] = 1 + char_tracker.get(n, 0)
    f.close()

    for n in char_tracker.keys():
        pq.put((char_tracker[n], TreeNode(n)))

    count = 0
    while pq.qsize() > 1:
        node1 = pq.get()
        node2 = pq.get()
        pq.put((node1[0] + node2[0], TreeNode(data = 'r' + str(count), left = node1[1], right = node2[1])))
        count += 1

    root = pq.get()[1]
    q.put((root, ''))
    w = open(sourcepath[:-4] + '/tree.txt', 'w')

    while not q.empty():
        node = q.get()

        if node[0].is_leaf():
            address_tracker[node[0].data] = node[1]
        else:
            writeString = str(node[0]) + ' '
            if node[0].left is not None:
                q.put((node[0].left, node[1] + '0'))
                writeString += str(node[0].left) + ' '
            else:
                writeString += '- '
            if node[0].left is not None:
                q.put((node[0].right, node[1] + '1'))
                writeString += str(node[0].right) + ' '
            else:
                writeString += '- '
            writeString = writeString.replace('\n', 'nl')
            writeString = writeString.replace('   ', ' sp ')
            w.write(writeString + '\n')
    w.close()
        
    f = open('./' + sourcepath, 'r')
    w = open(sourcepath[:-4] + '/' + 'data.bin', 'wb')
    writeString = ''
    for line in f:
        for n in line:
            writeString = writeString + address_tracker[n]
    w.write(bitarray(writeString))
    w.close()
    f.close()
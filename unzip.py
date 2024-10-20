from asyncore import write
from curses.ascii import BS
from operator import add
import numpy
import queue
from bitarray import bitarray
from tree import TreeNode

def unzip(sourcepath):
    pq = queue.PriorityQueue()
    q = queue.Queue()
    char_tracker = {}
    address_tracker = {}

    f = open(sourcepath + '/tree.txt', 'r')
    treeString = f.read()
    f.close()
    treeArr = treeString.split('\n')

    nodeHelper = {}
    splitstr = treeArr[0].split(' ')
    nodeHelper[splitstr[0]] = TreeNode(splitstr[0])

    for n in treeArr:
        if len(n) == 0:
            continue

        splitstr = n.split(' ')
        rNode = nodeHelper[splitstr[0]]

        if splitstr[1] != '-':
            rNode.left = TreeNode(splitstr[1])
            nodeHelper[splitstr[1]] = rNode.left
        if splitstr[2] != '-':
            rNode.right = TreeNode(splitstr[2])
            nodeHelper[splitstr[2]] = rNode.right

    root = nodeHelper[treeArr[0].split(' ')[0]]

    bString = "".join(f"{n:08b}" for n in open(sourcepath + '/data.bin', "rb").read())

    copyStr = ''
    searchNode = root
    # count = 0
    for b in bString:
        if b == '0':
            searchNode = searchNode.left
        else:
            searchNode = searchNode.right
        
        if searchNode.is_leaf():
            if searchNode.data == 'sp':
                copyStr += ' '
            elif searchNode.data == 'nl':
                copyStr += '\n'
            else:
                copyStr += searchNode.data
            searchNode = root

    f = open(sourcepath + '_copy.txt', 'w')
    f.write(copyStr)
    f.close()
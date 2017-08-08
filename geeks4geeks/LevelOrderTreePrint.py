from ds.MyTree import MyBinaryTree
from MyQueue import Queue
def printTreeLevel(mytree):
    if mytree == None:
        return
    queue = Queue()
    queue.enque(mytree)
    while (queue.size() > 0):
        newTree = queue.deque()
        print(newTree.get_root_val(),end=' ')
        if newTree.get_left_child() != None:
            queue.enque(newTree.get_left_child())
        if newTree.get_right_child() != None :
            queue.enque(newTree.get_right_child())

def printTreeLevelRec(queue):
    if queue.size() == 0:
        return
    newTree = queue.deque()

    print(newTree.get_root_val(), end=' ')
    if newTree.get_left_child() != None:
        queue.enque(newTree.get_left_child())
    if newTree.get_right_child() != None:
        queue.enque(newTree.get_right_child())

    printTreeLevelRec(queue)


def printTreeLevelSpiral(queue,direction):
    if queue.size() == 0:
        return
    newTree = queue.deque()

    print(newTree.get_root_val(), end=' ')
    if(direction):
        if newTree.get_left_child() != None:
            queue.enque(newTree.get_left_child())
        if newTree.get_right_child() != None:
            queue.enque(newTree.get_right_child())
    else:
        if newTree.get_right_child() != None:
            queue.enque(newTree.get_right_child())
        if newTree.get_left_child() != None:
            queue.enque(newTree.get_left_child())

    printTreeLevelSpiral(queue,not direction)





mytree2 = MyBinaryTree(10)
mytree2.insert_left(20)
mytree2.insert_right(30)
mytree2.get_left_child().insert_left(70)
mytree2.get_left_child().insert_right(60)
mytree2.get_right_child().insert_left(50)
mytree2.get_right_child().insert_right(40)


testQ = Queue()
testQ.enque(mytree2)
printTreeLevelSpiral(testQ,True)
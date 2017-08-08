from ds.MyTree import MyBinaryTree
def searchNodeAtDistance(mytree,dist):
    if mytree == None:
        return
    if dist == 0:
        print(mytree.get_root_val())
        return
    else:
        searchNodeAtDistance(mytree.get_right_child(), dist-1)
        searchNodeAtDistance(mytree.get_left_child(), dist - 1)



mytree = MyBinaryTree(1)
mytree.insert_left(2)
mytree.insert_right(3)
mytree.get_left_child().insert_left(4)
mytree.get_left_child().insert_right(5)
mytree.get_right_child().insert_left(8)


searchNodeAtDistance(mytree,2)


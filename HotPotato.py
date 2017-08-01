from MyQueue import Queue

def hot_potato(name_list,num):
    queue = Queue()
    for i in name_list:
        queue.enque(i)

    while queue.size() > 1:
        for i in range(num):
            queue.enque(queue.deque())
            if i == num - 1:
                queue.deque()

    return queue.deque()



names = ['user'+str(i) for i in range(11)]
print(hot_potato(names,7))
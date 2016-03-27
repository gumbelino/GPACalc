import re

class myLL:

    # myLL
    #    scope:     name:  type:
    #    private    tail   LLNode
    #    private    head   LLNode
    #    private    size   int

    def __init__(self):
        self.tail = LLNode(None)
        self.head =  LLNode(None)
        self.tail.next = self.head
        self.head.prev = self.tail
        self.__size = 0

    # add at the end method
    def add(self,elem):
        toAdd = LLNode(elem)
        if self.__size == 0:
            self.head.next = toAdd
            self.tail.prev = toAdd
            toAdd.next = self.tail
            toAdd.prev = self.head
        else:
            toAdd.next = self.tail
            toAdd.prev = self.tail.prev
            toAdd.prev.next = toAdd
            self.tail.prev = toAdd
        self.__size += 1

    # get method
    def get(self, index):
        if index < 0 or index >= self.size():
            return None
        curr = self.head.next
        for i in range(0, index):
            curr = curr.next
        return curr.data

    def addIndex(self, elem, index):

        if index > self.size() or index < 0:
            return

        if index == self.size() or self.size() == 0:
            self.add(elem)
            return

        toAdd = LLNode(elem)

        addBefore = self.head.next

        for i in range(0, index):
            addBefore = addBefore.next

        addBefore.prev.next = toAdd
        toAdd.prev = addBefore.prev
        addBefore.prev = toAdd
        toAdd.next = addBefore

        if index == 0:
            self.head.next = toAdd

        self.__size += 1

    # remove at the end method
    def remove(self):
        if self.__size > 0:
            toRemove = self.tail.prev
            toRemove.prev.next = self.tail
            self.tail.prev = toRemove.prev
            self.__size -= 1
            return toRemove.data

        else:
            return None

    # TODO: remove at the end method
    def removeIndex(self, index):
        if index >= self.size() or index < 0:
            return None

        if index == self.size()-1:
            return self.remove()

        toRemove = self.head.next
        for i in range(0, index):
            toRemove = toRemove.next

        toRemove.prev.next = toRemove.next
        toRemove.next.prev = toRemove.prev

        self.__size -= 1

        return toRemove.data


    # size method
    def size(self):
        return self.__size

    # write on file method
    def write(self, file):
        fid = open(file, 'w')
        curr = self.head.next
        for i in range (1, self.__size+1):
            fid.write(str(curr.data)+'\t')
            if i%10 == 0:
                fid.write('\n')
            curr = curr.next
        fid.close()

    # read from a file method
    def read(self, file):
        fid = open(file, 'r')
        for line in fid:
            li = line.strip()
            li = re.compile('\w+').findall(li)
            for elem in li:
                self.add(elem)
        fid.close()

    def printWithIndex(self):
        curr = self.head.next
        toPrint = ''
        for i in range (0, self.__size):
            toPrint += '(' + str(i+1) + ')'+ curr.data.__str__()
            if i < self.__size-1:
                toPrint += '\n'
            curr = curr.next
        return toPrint

    # print list method
    def __str__(self):
        curr = self.head.next
        toPrint = ''
        for i in range (0, self.__size):
            toPrint += curr.data.__str__()
            if i < self.__size-1:
                toPrint += '\n'
            curr = curr.next
        return toPrint

    def printBack(self):
        curr = self.tail.prev
        toPrint = ''
        for i in range (0, self.__size):
            toPrint += curr.data.__str__()
            if i < self.__size-1:
                toPrint += '\n'
            curr = curr.prev
        print(toPrint)


class LLNode:

    # LLNode
    #    scope:     name:  type:
    #    public     prev   LLNode
    #    public     next   LLNode
    #    protected  data   Whatever

    prev = None
    next = None

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


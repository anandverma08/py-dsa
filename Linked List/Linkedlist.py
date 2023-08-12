class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def insert(self, index, value):
        new_mode = Node(value)
        if index < 0 or index > self.length:
            return

        if self.length == 0:
            self.head = self.tail = new_mode
            self.length+=1
            return

        if index == 0:
            new_mode.next = self.head
            self.head = new_mode
            return
        i=0
        temp = self.head
        while i < index-1:
            temp = temp.next
            i+=1

        new_mode.next = temp.next
        temp.next = new_mode
        self.length+=1

    def traverse(self):
        current = self.head
        res = []
        while current:
            res.append(current.value)
            current = current.next
        return res

    def search(self, value):
        current = self.head
        i = 0
        while current:
            if current.value == value:
                return i
            else:
                current = current.next
                i+=1
        return -1

    def get(self, index):
        if index < 0 or index > self.length:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set(self, index, value):
        current = self.get(index)
        if current:
            current.value = value

    def pop_first(self):
        if self.length ==0:
            return False
        current = self.head
        if self.length ==1:

            self.head = None
            self.tail = None
            return current.value

        self.head = current.next
        current.next = None
        self.length-=1
        return current.value

    def pop(self):
        if self.length ==0:  return False
        last_node = self.tail
        if self.length ==1:
            self.head = self.tail = None
            return last_node
        current = self.head
        while current.next is not last_node:
            current = current.next
        current.next = None
        self.tail = current
        self.length-=1
        return last_node.value

    def remove(self, index):
        if self.length==0: return False
        last_node = self.tail
        if self.length==1:
            self.head = self.tail = None
            return last_node
        prev_node = self.get(index - 1)
        current = prev_node.next

        prev_node.next = current.next
        current.next = None
        self.length-=1
        return current

    def deleteAll(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result+="->"
            temp_node=temp_node.next
        return result

    def reverse(self):
        current = self.head
        prev = None
        print(current.next)
        print(self.tail.next)
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head, self.tail = self.tail, self.head


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.prepend(5)
# linked_list.insert(-1,15)
# print(linked_list.traverse())
# print(linked_list.search(50))
# print(linked_list.get(-3))
# linked_list.set(2,16)
# print(linked_list.pop())
# linked_list.remove(1)
linked_list.reverse()
print(linked_list)






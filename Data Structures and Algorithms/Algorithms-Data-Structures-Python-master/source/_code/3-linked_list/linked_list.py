class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
            if tmp:
                print("-> ", end=" ")
        print()

    def append(self, value):
        # O(1) if know the tail
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        # O(1)
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop_first(self):
        # O(1)
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return

        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        return tmp

    def pop(self):
        # O(N)
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None
        self.tail = temp
        return temp

    def reverse(self, head):
        # # O(N)
        # if self.head == None:
        #     return
        # if self.head.next == None:
        #     return

        # prev = None
        # curr = self.head
        # after = curr.next

        # while after:
        #     curr.next = prev
        #     prev = curr
        #     curr = after
        #     after = after.next

        # curr.next = prev
        # self.head, self.tail = self.tail, self.head
        if not self.head:
            return None

        new_head = self.head
        if self.head.next:
            new_head = self.reverse(head=self.head.next)
            self.head.next.next = self.head

        self.head.next = None
        return new_head


if __name__ == "__main__":

    linkedlist = LinkedList()
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)

    linkedlist.print_list()
    linkedlist.prepend(0)
    linkedlist.print_list()

    linkedlist.reverse(linkedlist.head)

    linkedlist.print_list()

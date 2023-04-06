class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def Insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("the list is empty")

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data)+"-->"
            itr = itr.next
        print(llstr)

if __name__ == "__main__":
    ll = LinkedList()
    ll.Insert_at_beginning(23)
    ll.Insert_at_beginning(34)
    ll.Insert_at_beginning(234)
    ll.Insert_at_beginning(834)
    ll.Insert_at_beginning(583)
    ll.print()

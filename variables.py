class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __int__(self):
        self.head = None

    def insert_at_beginnig(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("there is no element in the linked list")

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_at_end (self,data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def inser_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return (counter)

if __name__ == "__main__":
    ll = LinkedList()
    ll.inser_values(["banana", "mango", "grapes", "orange"])
    ll.get_length()
    ll.print()

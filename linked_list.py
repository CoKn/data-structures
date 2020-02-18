class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        n = 0
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            n += 1
        return n

    def display(self):
        linked_list = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            linked_list.append(current_node.data)
        return linked_list

    def get_elem(self, index):
        if index >= self.length():
            print('Index is out of range!')
        else:
            current_node = self.head
            pointer = 0
            while pointer <= index:
                current_node = current_node.next
                pointer += 1
            return current_node.data

    def delete(self, index):
        if index >= self.length():
            print('Index is out of range!')
        else:
            pointer = 0
            current_node = self.head
            while True:
                last_node = current_node
                current_node = current_node.next
                if pointer == index:
                    last_node.next = current_node.next
                    break
                pointer += 1

    def insert(self, index, data):
        if index >= self.length():
            print('Index is out of range!')
        else:
            pointer = 0
            new_node = Node(data)
            current_node = self.head
            while True:
                current_node = current_node.next
                if pointer == index:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    break
                pointer += 1

    def merge(self, index, linked_list):
        if index >= self.length():
            print('Index is out of range!')
        else:
            pointer = 0
            current_node = self.head
            while True:
                current_node = current_node.next
                if pointer == index:
                    linked_list_node = linked_list.head
                    while linked_list_node.next is not None:
                        linked_list_node = linked_list_node.next
                    linked_list_node.next = current_node.next
                    current_node.next = linked_list.head.next
                    break
                pointer += 1

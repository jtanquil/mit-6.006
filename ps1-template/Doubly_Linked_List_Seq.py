class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        # if first element, set the head and tail to the node
        # otherwise, set self.head = new_head, old_head.prev = new_head, new_head.next = old_head
        new_head = Doubly_Linked_List_Node(x)

        if self.head is None and self.tail is None:
            self.head = new_head
            self.tail = new_head
        else:
            old_head, self.head = self.head, new_head
            new_head.next, old_head.prev = old_head, new_head

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        # if first element, set the head and tail to the node
        # otherwise, set self.tail = new_tail, old_tail.next = new_tail, new_tail.prev = old_tail
        new_tail = Doubly_Linked_List_Node(x)

        if self.head is None and self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            old_tail, self.tail = self.tail, new_tail
            new_tail.prev, old_tail.next = old_tail, new_tail

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        # if there's one element, set both head and tail to None
        # otherwise, set self.head.next to be the new head
        if self.head is None:
            return x
        else:
            old_head = self.head
            x = old_head.item

            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                new_head = old_head.next
                new_head.prev = None
                self.head = new_head
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        # if there's one element, set both head and tail to None
        # otherwise, set self.tail.prev to be the new tail
        if self.tail is None:
            return x
        else:
            old_tail = self.tail
            x = old_tail.item

            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                new_tail = old_tail.prev
                new_tail.next = None
                self.tail = new_tail
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        # connect x1.prev <-> x2.next
        # edge cases: x1 as the head, x2 as the tail, x1.prev/x2.next are None
        # x1 none: like arr[:x2] (including x2), x2 none: like arr[x1:]
        if x1 is None:
            x1 = self.head
        
        if x2 is None:
            x2 = self.tail

        L2.head = x1
        L2.tail = x2

        if x1 == self.head:
            self.head = x2.next
        
        if x2 == self.tail:
            self.tail = x1.prev

        if x1.prev is not None:
            x1.prev.next = x2.next
        
        if x2.next is not None:
            x2.next.prev = x1.prev

        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        # set x <-> L2.head <-> ... <-> L2.tail <-> x.next
        # edge case: x.next = None => set self.tail = L2.tail
        old_next = x.next
        x.next, L2.head.prev = L2.head, x

        if old_next is None:
            self.tail = L2.tail
        else:
            L2.tail.next = old_next
            old_next.prev = L2.tail

        L2.head = None
        L2.tail = None
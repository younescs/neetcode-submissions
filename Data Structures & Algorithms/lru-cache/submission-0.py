class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(0)
    
    def get(self, key):
        if key in self.cache:
            prev = self.head
            tail = self.head.next
            while tail and tail.val != key:
                prev = tail
                tail = tail.next
            prev.next = tail.next
            tail.next = self.head.next
            self.head.next = tail
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            prev = self.head
            tail = self.head.next
            while tail and tail.val != key:
                prev = tail
                tail = tail.next
            prev.next = tail.next
            tail.next = self.head.next
            self.head.next = tail
            self.cache[key] = value
        
        else:
            self.cache[key] = value
            node = ListNode(key)
            node.next = self.head.next
            self.head.next = node
            if len(self.cache) > self.capacity:
                prev = self.head
                curr = self.head.next
                while curr.next:
                    prev = curr
                    curr = curr.next
                prev.next = None
                del self.cache[curr.val]
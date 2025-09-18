# Last updated: 19/09/2025, 00:18:08
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def add_to_head(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

    def remove_node(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove_node(node)
            self.add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.remove_node(node)
            self.add_to_head(node)
        else:
            if len(self.cache)>=self.capacity:
                lru=self.tail.prev
                self.remove_node(lru)
                del self.cache[lru.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_to_head(new_node)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
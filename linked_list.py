class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next
        
    def get_next(self):
        return self.next
    
    def get_node_info(self):
        return (self.data, self.next)
    
class linked_list:
    def __init__(self):
        self.linked_list = []
    
    def add(self, node: Node):
        self.linked_list.append(node)
    
    def get_header(self):
        return self.linked_list[0]
    
    def get_linked_list(self):
        return self.linked_list
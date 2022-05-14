""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def traversal(node, values):
    
    
    if node is not None:
        
        values = traversal(node.left, values)
        values.append(node.data)
        values = traversal(node.right, values)
        
        
    return values
    
    
    
        
        

def check_binary_search_tree_(root):
    
    values = []
    
    traversal(root, values)
    
    for i in range(len(values) - 1):
        
        if values[i] >= values[i + 1]:
            return False
        
    return True
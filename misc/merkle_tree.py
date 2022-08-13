class MerkleNode():
    def __init__(self):
        self.hash = None
        self.right = None
        self.left = None

def verify_tree(t):
    if t.left == None and t.right == None:
        return True
    a = t.hash == hash(t.left.hash + t.right.hash)
    b = verify_tree(t.left)
    c = verify_tree(t.right)
    return a and b and c

def print_tree(t):
    if t == None:
        return
    print_tree(t.left)
    print(t.hash)
    print_tree(t.right)

def create_tree(data):
    l = len(data)
    middle = int(l / 2)
    t = MerkleNode()
    
    if l == 0:
        t.hash = ''
        return t
    elif l == 1:
        t.hash = data[0]
        return t
    else:
        t.left = create_tree(data[ :middle])
        t.right = create_tree(data[middle: ])
        t.hash = hash(t.left.hash + t.right.hash)
        return t

data = [1, 2, 3, 4, 5, 6, 7, 8]

a = create_tree(data)
print_tree(a)
print(verify_tree(a))
a.hash = -1
print(verify_tree(a))
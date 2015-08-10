'''Implement a function to check if a binary tree is balanced. For the purposes of this
question, a balanced tree is defined to be a tree such that the heights
of the two subtrees of any node never differ by more than one.'''

class BinTree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def addNode(self,key):
        if key<=self.key:
            if self.left:
                self.left.addNode(key)
            else:
                self.left=BinTree(key)
        else:
            if self.right:
                self.right.addNode(key)
            else:
                self.right=BinTree(key)
        
def isBalanced(tree):
    # returns balanced if the tree is balanced else false
    if tree==None:
        return True
    else:
        if isBalanced(tree.left) and isBalanced(tree.right) and abs(height(tree.left)-height(tree.right))<=1:
            return True
        else:
            return False

def height(tree):
    # returns the height of the tree
    if not tree:
        return 0
    else:
        return max(height(tree.left),height(tree.right))+1

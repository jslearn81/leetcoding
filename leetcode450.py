# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TAGS: BST
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def delBST(node):

            if not node:
                return(None)

            if node.val>key:
                node.left = delBST(node.left)
                return(node)
            elif node.val<key:
                node.right = delBST(node.right)
                return(node)
            
            #skip and return if only one children or none.
            if node.left is None:
                return(node.right) 
            elif node.right is None:
                return(node.left)
            
            #have both children
            #find successor
            parent = node
            succ = node.right
            while (succ.left):
                parent = succ
                succ = succ.left
            
            node.val = succ.val
            if parent != node:
                parent.left = succ.right
            else:
                parent.right = succ.right
            
            del succ
            return(node)
        
        return(delBST(root))



            

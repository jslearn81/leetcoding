#TAG: BST
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root:
            if val > root.val:
                root.right = self.insertIntoBST(root.right,val)
                return(root)
            elif val < root.val:
                root.left = self.insertIntoBST(root.left,val)
                return(root)
        else:
            return(TreeNode(val=val))

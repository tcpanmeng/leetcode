# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = True
        global preval
        preval = None
        if not root:
            return True
        else:
            if not preval:
                preval = root.val
        if root.left:
            self.isValidBST(root.left)
        print(root.val,':',preval)
        # if root.val >= preval:
        #     return False
        if root.right:
            self.isValidBST(root.left)
        return True
    

if __name__ == "__main__":
    tree = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree7 = TreeNode(7)
    tree.left = tree2
    tree.right = tree3
    tree2.left = tree7
    tree3.left = tree4
    tree3.right = tree5
    tree4.left = tree6
    s = Solution()
    print("98_验证二叉搜索树",s.isValidBST(tree))
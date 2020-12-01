# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal_dc(self, root:TreeNode)->[int]:
            if root is None:
                return [] 
            res = []
            if root:
                res.append(root.val)
            if root.left:
                res.extend(self.preorderTraversal(root.left))
            if root.right:
                res.extend(self.preorderTraversal(root.right))
            return res


    def preorderTraversal(self, root:TreeNode)->[int]:    
        if root is None:
            return []
        stack = [root]
        res = []
        node = None
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
    # 中序遍历 递归实现
    def inorderTraversal_dc(self, root: TreeNode) -> [int]:
        if root is None:
            return []
        return self.inorderTraversal_dc(root.left)+[root.val]+self.inorderTraversal_dc(root.right)
    def inorderTraversal(self,root:TreeNode) ->[int]:
        if root is None:
            return []
        res = []
        cur = root
        stack = []
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
    # 后序遍历
    def postorderTraversal_dc(self,root:TreeNode)-> [int]:
        if root is None:
            return []
        return self.postorderTraversal_dc(root.left)+self.postorderTraversal_dc(root.right)+[root.val]
    # 循环方法
    def postorderTraversal(self,root:TreeNode) -> [int]:
        if root is None:
            return []
        res = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()
        return res[::-1]    

if __name__ == "__main__":
    tree = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree.left = tree2
    tree.right = tree3
    tree3.left = tree4
    tree3.right = tree5
    tree4.left = tree6
    s = Solution()

    print(s.preorderTraversal(tree))
    print("中序遍历",s.inorderTraversal(tree))
    print("后序遍历-递归",s.postorderTraversal_dc(tree))
    print("后序遍历-循环",s.postorderTraversal(tree))
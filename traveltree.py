from queue import Queue
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
    # 层次遍历，广度优先
    def levelOrderTraversal(self,root:TreeNode) ->[[int]]:
        q = Queue()
        if root is None:
            return [[]]
        res = []
        q.put(root)
        while not q.empty():
            re = []
            nextQueue = Queue()
            while not q.empty():
                cur = q.get()
                re.append(cur.val)
                if cur.left:
                    nextQueue.put(cur.left)
                    
                if cur.right:
                    nextQueue.put(cur.right)
            q = nextQueue
            res.append(re)
            
        return res
        
    def isValidBST(self, root: TreeNode) -> bool:
        res = s.inorderTraversal(root)
        print(res)
        # 再判断数组是否是有序的
        for i in range(1,len(res)):
            if res[i-1]>res[i]:
                return False
        return True
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        prenode = None
        stack =[root]
        cur = None

        while stack or cur:
            cur 
            prenode = root.left
            prenode.right = root
            prenode.left = None
            root = prenode
        
        while root.right:
            prenode = root
            root = prenode
            
        return root



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

    # print("前续遍历",s.preorderTraversal(tree))
    # print("中序遍历",s.inorderTraversal(tree))
    # print("后序遍历-递归",s.postorderTraversal_dc(tree))
    # print("后序遍历-循环",s.postorderTraversal(tree))
    # print("层次遍历",s.levelOrderTraversal(tree))
    # print("98_验证二叉搜索树",s.isValidBST(tree))
    print("98_验证二叉搜索树",s.convertBiNode(tree))


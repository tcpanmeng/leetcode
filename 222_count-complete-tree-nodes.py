# 222 完全二叉树节点个数
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right :
            return 1
        
        # 根据位置查找遍历，5 = 101，不看第一位，也就是01，0表示向左，1表示向右，
        def exist_mid(root, level, mid):
            bits, node = 1 << (level - 1), root
            while node and bits > 0:
                if bits & mid:
                    node = node.right
                else:
                    node = node.left
                bits >>= 1
            return node

        # 求深度
        depth ,node = 0,root
        while(node.left):
            depth += 1
            node = node.left

        # 遍历根结点
        left = 1 << depth
        right = (1 << (depth+1))-1
        mid = 0
        while left < right:
            mid = (right +left) // 2
            if exist_mid(root,depth,mid):
                left = mid+1
            else:
                right = mid
        if exist_mid(root,depth,left):
            return left
        else:
            return left-1

        

if __name__ == "__main__":
    tree = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree.left = tree2
    tree.right = tree3
    tree2.left = tree4
    tree2.right = tree5
    tree3.left = tree6
    tree3.right = TreeNode(7)
    s = Solution()
    print(s.countNodes(tree))
    

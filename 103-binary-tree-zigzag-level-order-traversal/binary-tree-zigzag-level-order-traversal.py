# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        n = 0
        while queue:
            n +=1
            result = []
            level_size = len(queue)
            for _ in range(level_size):
                root = queue.popleft()
                result.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            if not n %2:

                result.reverse()
            ans.append(result)


        return ans

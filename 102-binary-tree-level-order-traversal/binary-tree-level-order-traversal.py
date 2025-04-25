from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        level = 0
        current_l = []
        queue = deque([(root,0)])

        while queue:
            node,node_level = queue.popleft()
            if not node:
                continue
            if node_level != level:
                levels.append(current_l.copy())
                current_l = []
                level +=1


            current_l.append(node.val)
            queue.append((node.left,level+1))
            queue.append((node.right,level+1))
        if current_l:

            levels.append(current_l.copy())

        return levels



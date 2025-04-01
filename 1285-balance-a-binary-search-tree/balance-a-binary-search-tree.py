# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)


        def arr(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = arr(nums[:mid])
            node.right = arr(nums[mid+1:])
            return node  

        return arr(result)  

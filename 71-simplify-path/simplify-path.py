class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for char in path.split('/'):
            if not char or char == '.':

                continue
            elif char == '..':
                if stack:
                    stack.pop()
               
            else:
                stack.append(char)

        simplified_path = '/' + '/'.join(stack)

        return simplified_path
                
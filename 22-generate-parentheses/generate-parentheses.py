class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def validPar(par):
            st = []
            for p in par:
                if p == '(':
                    st.append(p)
                else:
                    if not st:
                        return False
                    st.pop()
            return not st
        def backtrack(par):
            if len(par) == n*2:
                if validPar(par[:]):
                    ans.append(''.join(par))
                return
            
            backtrack(par+['('])
            backtrack(par+[')'])
        backtrack([])
        
        return ans
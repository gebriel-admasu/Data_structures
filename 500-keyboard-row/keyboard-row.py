class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        dic = {
            "row1": "qwertyuiop",
            "row2": "asdfghjkl",
            "row3": "zxcvbnm"
        }

        for word in words:
            word_lower = word.lower()  
            yes = True

            if word_lower[0] in dic["row1"]:
                for char in word_lower:
                    if char not in dic["row1"]:
                        yes = False
                        break
            elif word_lower[0] in dic["row2"]:
                for char in word_lower:
                    if char not in dic["row2"]:
                        yes = False
                        break
            elif word_lower[0] in dic["row3"]:
                for char in word_lower:
                    if char not in dic["row3"]:
                        yes = False
                        break

            if yes:
                res.append(word)

        return res
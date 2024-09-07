class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        j = 0
        c_str = ''
        count = 0
        
        while True:
            if len(strs) > 1:
                if strs[i][j] == strs[i+1][j]:
                    count += 1
                    if strs[i+1] == strs[-1]:
                        if count == len(strs) - 1:
                            c_str += strs[i][j]
                            count = 0
                            j += 1
                            i = -1
                        else:
                            break
                else:
                    break
                i += 1
            else:
                c_str = strs[i]
                break
        return c_str

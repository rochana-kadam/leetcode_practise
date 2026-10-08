class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs==[""]:
            return ""
        small=min(strs,key=len)
        for i in range (len(small)):
            for j in range (len(strs)):
                if strs[j][i]!=small[i]:
                    return small[:i]
                    
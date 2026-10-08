class Solution(object):
    def romanToInt(self, s):
        val=0
        values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range (len(s)):
            v1=values[s[i]]

            if i==len(s)-1:
                val+=v1
                break

            v2=values[s[i+1]]

            if v1>=v2:
                val+=v1
            elif v1<v2:
                val-=v1

        return val       

        # val = 0
        # for i in range(len(s)):
        
        #     if s[i] == 'I':
        #         v1 = 1
        #     elif s[i] == 'V':
        #         v1 = 5
        #     elif s[i] == 'X':
        #         v1 = 10
        #     elif s[i] == 'L':
        #         v1 = 50
        #     elif s[i] == 'C':
        #         v1 = 100
        #     elif s[i] == 'D':
        #         v1 = 500
        #     elif s[i] == 'M':
        #         v1 = 1000

        #     if i == len(s) - 1:
        #         val += v1
        #         break

        #     if s[i + 1] == 'I':
        #         v2 = 1
        #     elif s[i + 1] == 'V':
        #         v2 = 5
        #     elif s[i + 1] == 'X':
        #         v2 = 10
        #     elif s[i + 1] == 'L':
        #         v2 = 50
        #     elif s[i + 1] == 'C':
        #         v2 = 100
        #     elif s[i + 1] == 'D':
        #         v2 = 500
        #     elif s[i + 1] == 'M':
        #         v2 = 1000

        #     if v1 < v2:
        #         val -= v1
        #     else:
        #         val += v1

        # return val
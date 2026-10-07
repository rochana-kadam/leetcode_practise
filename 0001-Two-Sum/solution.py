class Solution(object):
    def isPalindrome(self, x):
        y=x
        new=0
        while x>0:
           new= (new*10)+x%10
           x=x/10
        if new==y:
            return True
        else:
            return False

        
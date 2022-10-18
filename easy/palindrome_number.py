class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==0: 
            return True
        
        if (x<0) or (x%10==0):
            return False
        
        r=0
        
        while(x>r):
            r = (r*10) + (x%10)
            x = x//10
            
        return (x==r) or (x==r//10)


# Solution 1 -> Convert int to string, then check reverse of string = original string
# def isPalindrome(self, x: int) -> bool:
#   n=str(x)
#   return n[::-1] == n

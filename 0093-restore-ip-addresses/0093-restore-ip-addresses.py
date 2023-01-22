class Solution:
    def restoreIpAddresses(self, s):
        def helper(pre, post):
            if len(pre) == 4:
                if not post: # find a valid IP
                    ans.append( "".join(i+"." for i in pre)[:-1]) 

            elif post:
                helper(pre + [post[:1]], post[1:]) # One digit     
                if post[0] != "0": # Two and Three digits
                    if len(post[:2]) == 2: 
                        helper(pre + [post[:2]], post[2:])
                    if len(post[:3]) == 3 and 0 <= int(post[:3]) <= 255: 
                        helper(pre + [post[:3]], post[3:])
        ans = []
        helper([], s)
        return ans
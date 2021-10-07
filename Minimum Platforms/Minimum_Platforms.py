"""

https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#

sort both arr and dep
then move with two pointer approch 


"""


class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        max_count = 0
        curr_count = 0
        arr.sort()
        dep.sort()
        p1 = p2 = 0
        while p1 < n:
            if arr[p1] <= dep[p2]:
                curr_count+=1
                p1+=1
            else:
                curr_count-=1
                p2+=1
            max_count = max(curr_count,max_count)
        return max_count
        


"""
https://leetcode.com/problems/push-dominoes/


Sol:-
There could be four case between two points A and B

A....B  
L....L ==> all points will have effect of L ==> LLLLL
R....R ==> all points will have effect of R ==> RRRRR
L....R ==> pushing Left and pushing Right , won't have any impact on middile dominos , hence continue
R....L ==> Left Half will have R effect andf Right half will have L effect.


Use j as finding right side L/R.
"""




class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        i = 0
        j = i+1
        dominoes = [ch for ch in 'L'+ dominoes + 'R']
        n = len(dominoes)
        while j < n:
            while dominoes[j] == '.':
                j+=1
            if (j - i) > 1:
                if dominoes[i] == 'L' and dominoes[j] == 'L':
                    for k in range(i+1,j):
                        dominoes[k] = 'L'
                        
                elif dominoes[i] == 'R' and dominoes[j] == 'R':
                    for k in range(i+1,j):
                        dominoes[k] = 'R'
                        
                elif dominoes[i] == 'L' and dominoes[j] == 'R':
                    pass
                else:
                    k = 1
                    while i+k < j-k:
                        dominoes[i+k] = 'R'
                        dominoes[j-k] = 'L'
                        k+=1
            i = j
            j+=1
        return ''.join(dominoes[1:n-1])

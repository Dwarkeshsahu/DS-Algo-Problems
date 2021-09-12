"""
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106


Summary:-
Query is large , so find all prime at once and do query 

Sol:=
Make an boolean(True) array of n length.
Run loop from 2 to sqrt(n) and mark False all the multiple of this range in boolean array , as they will be a multiple of 2 to sqrt(n) range.
Now all True element remain in boolean array will be prime numbers

"""



class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True for _ in range(n)]
        i = 2
        while i*i < n:
            if isPrime[i] is False:
                i+=1
                continue
            j = 2*i
            while j < n:
                isPrime[j] = False
                j+=i
            i+=1
        count = 0
        for i in range(2,n):
            if isPrime[i] is True:
                count+=1
        return count



# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n < 2:
#             return 0
#         isPrime = [True for _ in range(n+1)]
#         isPrime[0] = False
#         isPrime[1] = False
#         # print("isPrime", isPrime)
#         primeFactors = [x for x in range(2,int(sqrt(n))+1)]
#         for factor in primeFactors:
#             if isPrime[factor] == False:
#                 continue
#             i = 2
#             while factor*i <= n:
#                 isPrime[factor*i] = False
#                 i+=1
#         count = 0
#         for i in range(n):
#             if isPrime[i] == True:
#                 count+=1
#         return count

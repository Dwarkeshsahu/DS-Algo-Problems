"""
A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 

Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
 

Constraints:

num1 and num2 are valid complex numbers.




"""

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = num1.split('+')
        a2, b2 = num2.split('+')
        
        a1 = int(a1)
        b1 = int(b1[:-1])
        a2 = int(a2)
        b2 = int(b2[:-1])
        newa = (a1*a2 -b1*b2)
        newb = (a1*b2 +b1*a2)
        return str(newa)+str('+') + str(newb)+'i'

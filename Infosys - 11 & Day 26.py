#code:
#Check for Power
import math
class Solution:
    def isPowerOfAnother(ob,X,Y):
        if X==1:
            return 1 if Y==1 else 0
        power=math.log(Y)/math.log(X)
        return 1 if power.is_integer() or abs(power-round(power))<1e-9 else 0


#OUTPUT:
Input:
X = 2, Y = 8
Output:
1
Explanation:
23 is equal to 8.
Input:
X = 1, Y = 8
Output:
0
Explanation:
Any power of 1 is not 
equal to 8.

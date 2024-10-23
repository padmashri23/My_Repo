#program to implement heapsort by pushing all values onto a heap and then popping off the smallest values one at a time.
import heapq as hq
def heapsort(iterable):
    h=[]
    for value in iterable:
        hq.heappush(h,value)
    return[hq.heappop(h)for i in range(len(h))]
print(heapsort([7,89,54,6,2,3,1,5,7,5,9,6,3,2,4,15,25,3,6,36,2,6,24]))

#OUTPUT:
[1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 7, 7, 9, 15, 24, 25, 36, 54, 89]

#Mean:
import math
class Solution:
    def mean(self,N,A):
        total=sum(A)
        return math.floor(total/N)

#OUTPUT:
For Input: 
4
56 67 30 79
Your Output: 
58


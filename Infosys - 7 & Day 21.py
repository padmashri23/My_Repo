#CODE:
#Party of Couples
class Solution:
    def findSingle(self,n,arr):
        result=0
        for n in arr:
            result^=n
        return result

#XOR Operation: Loop through each number in the array and apply the XOR operation with result. This will cancel out all the paired numbers.

#OUTPUT:
#Input: 
#n = 5
#arr = {1, 2, 3, 2, 1}
#Output: 
#3
#Explaination: Only the number 3 is single.
#Example 2:

#Input: 
#n = 11 
#arr = {1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6} 
#Output: 
#4 
#Explaination: 4 is the only single.

#Write a Python function that accepts an arbitrary list and converts it to a heap using the heap queue algorithm.
import heapq as hq
raw_heap=[25, 44, 68, 21, 39, 23, 89]
print("Raw heap:",raw_heap)
hq.heapify(raw_heap)
print("heapified heap:",raw_heap)

#OUTPUT:
#Raw heap: [25, 44, 68, 21, 39, 23, 89]
#heapified heap: [21, 25, 23, 44, 39, 68, 89]






#Middle of Three:

class Solution:
    def middle(self,A,B,C):
        if(A>B and A<C) or (A>C and A<B):
            return A
        elif(B>A and B<C) or (B>C and B<A):
            return B
        else:
            return C
#For Input: 
978 518 300
#Your Output: 
518

#Python: Push three items into the heap and print the items from the heap
import heapq
heap=[]
heapq.heappush(heap,('V',1))
heapq.heappush(heap,('V',2))
heapq.heappush(heap,('V',3))
for a in heap:
    print(a)

#OUTPUT:
('V', 1)
('V', 2)
('V', 3)



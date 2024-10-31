#Python program to push three items into a heap and return the smallest item from the heap. Also, pop and return the smallest item from the heap.

import heapq
heap=[]
heapq.heappush(heap,('V',3))
heapq.heappush(heap,('V',2))
heapq.heappush(heap,('V',1))
print("The items in the heap are:")
for a in heap:
    print(a)
print("---------------------------")
print("The smallest element in the heap is:")
print(heap[0])
print("---------------------------")
print("the poped out items are:")
heapq.heappop(heap)
for a in heap:
    print(a)


#OUTPUT:
The items in the heap are:
('V', 1)
('V', 3)
('V', 2)
---------------------------
The smallest element in the heap is:
('V', 1)
---------------------------
the poped out items are:
('V', 2)
('V', 3)

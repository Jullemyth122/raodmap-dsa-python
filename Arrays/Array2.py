import heapq

def second_max(nums):

    if not nums:
        return None
    if len(nums) == 1:
        return None
        
    max1 = max2 = float('-inf');
    
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif max1 > num and max2 < num:
            max2 = num

            
    # print(max2, max1)
    # print(max2 != max1)
    return max2 if max2 != float('-inf') else None # if all equal → no real second max

def third_max(nums):

    if(len(nums) < 3): 
        return None

    max1 = max2 = max3 = float('-inf');
    
    for num in nums:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num

        elif max1 > num and max2 < num:
            max3 = max2
            max2 = num

        elif num > max3 and max2 > num:
            max3 = num
            
    # print(max2, max1)
    # print(max2 != max1)
    # return max2 if max2 != float('-inf') else None # if all equal → no real second max
    return max3 if max3 != float('-inf') else None # if all equal → no real second max

def nth_max(nums, k):
    if( k < 1 or len(nums) < k):
        return None

    maxes = [float('-inf')] * k

    # print(maxes)

    for num in nums:

        if num in maxes:
            print(num, maxes)
            continue 

        for i in range(k):
            if num > maxes[i]:
                maxes[i+1:] = maxes[i:-1]
                maxes[i] = num
                break

        # print(maxes)

    return maxes[-1] if maxes[-1] != float('-inf') else None

def nth_largest_heap(nums, k):
    if k < 1 or len(nums) < k:
        return None
        
    # min-heap of the k largest numbers
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)   # pop + push in one operation
            
    return heap[0] if heap else None

# def nth_max(nums, k):

#     if k < 1:
#         return None

#     maxes = []

#     for num in nums:

#         if num in maxes:
#             continue

#         maxes.append(num)
#         maxes.sort(reverse=True)

#         if len(maxes) > k:
#             maxes.pop()

#     # return maxes[-1] if len(maxes) == k else None
#     return maxes

if __name__ == "__main__":
    
    # x = second_max([7,7,7,1])
    # x = third_max([7,7,7,1,2])
    x = nth_max([7,7,7,1,2], 2)
    print(x)
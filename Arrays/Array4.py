def reverseList(arr):
    
    # left, right = 0, len(arr) - 1

    # while (left < right):
    #     arr[left], arr[right] = arr[right], arr[left]
    #     left += 1
    #     right -= 1

    # return arr
    for i in range(len(arr)):
        last = arr.pop();
        arr.insert(i, last);
    
    return arr
        

if __name__ == "__main__":
    arr = [1,2,3,4,4,5]
    x = reverseList(arr)
    print(x)
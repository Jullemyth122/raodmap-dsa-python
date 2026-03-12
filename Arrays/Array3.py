from typing import Sequence

def ctEvenNumbers(arr):

    ct = 0
    for i in range(len(arr)):
        if(arr[i] % 2 == 0):
            ct += 1;
    return ct

def count_even_numbers(numbers: Sequence[int]) -> int:
    return sum(1 for x in numbers if not x & 1)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    # x = ctEvenNumbers(arr)
    x = count_even_numbers(arr)
    print(x)
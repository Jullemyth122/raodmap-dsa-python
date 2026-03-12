def ValinPalindrome(_string):
    
    # left, right = 0, len(_string) - 1

    # while (left < right):
    #     if (_string[left] != _string[right]):
    #         return False
    #     left += 1
    #     right -= 1

    # return True
    cleaned = [c.lower() for c in _string if c.isalnum()]
    
    reversed_version = []
    temp = cleaned[:]
    print(temp)
    while temp:
        reversed_version.append(temp.pop())

    return cleaned == reversed_version

if __name__ == "__main__":
    _string = "lolol"
    x = ValinPalindrome(_string)
    print(x)
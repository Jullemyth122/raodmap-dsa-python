def RunningSum(res):

    # newRes = []
    # j = 0;
    # for i in res:
    #     j += i
    #     newRes.append(j);  
    
    # return newRes
    if not res:
        return res;

    for i in range(1, len(res)):
        res[i] += res[i - 1];


    return res

if __name__ == "__main__":
    
    x = RunningSum([1,2,3,4])
    print(x)

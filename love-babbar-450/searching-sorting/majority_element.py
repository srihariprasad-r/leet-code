def majorityElement(arr):
    n = len(arr)
    
    map = {}
    
    for i in range(len(arr)):
        if not(arr[i]) in map:
            map[arr[i]] = 1
        else:
            map[arr[i]] += 1
        
    for k, v in map.items():
        if v > n //2:
            return k
    
arr = [3,1,3,3,2]
print(majorityElement(arr))
class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        new_array = []        
        
        def func(arr, m, k):
            if m > 1:
                for i in range(0,len(arr),m):
                    if len(new_array) == 0:
                        new_array.append(arr[i:i+m])
                    elif ((new_array[-1] == arr[i:i+m]) or (new_array[-1] == arr[i:i+m][::-1])):
                        new_array.append(arr[i:i+m])
                    else:
                        if len(new_array) < k and len(new_array) > 0:
                            new_array.pop()
                print(new_array)
                return len(new_array)
            
            else:                                        
                for i in range(len(arr)-1):
                    if len(new_array) == 0:
                        new_array.append(arr[i])
                    
                    if arr[i] == arr[i+1]:
                        new_array.append(arr[i])
                    else:
                        if len(new_array) < k and len(new_array) > 0:
                            new_array.pop()

                return len(new_array)        
            
        output = func(arr, m, k)

        if output >= k:
            return True
        else:
            return False            
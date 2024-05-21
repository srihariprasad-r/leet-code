# wrong submission
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        s = 0

        for i in range(len(arr)):
            s += arr[i]

        def kadane(a):
            csum = a[0]
            msum = a[0]            
            for i in range(1,len(a)):
                if csum + a[i] > a[i]:
                    csum += a[i]
                else:
                    csum = a[i]

                if msum < csum:
                    msum = csum

            return msum

        def kadanes2(a):
            n = [0] * (len(a)*2)

            for i in range(len(a)):
                n[i] = a[i]

            for i in range(len(a)):
                n[i+len(a)] = a[i]

            return kadane(n)

        if k == 1:
            return kadane(arr)
        elif s < 0:
            return kadanes2(arr)
        else:
            return kadanes2(arr) + (k-2)*s
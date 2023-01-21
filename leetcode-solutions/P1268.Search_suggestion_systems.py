# wrong submission

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        def bs(target):
            l = 0
            r = len(products)

            while l < r:
                m = (l + r)//2
                # if products[m][:len(target)] == target:
                #     return m

                if products[m] > target:
                    r = m - 1
                else:
                    l = m + 1

            return l

        ans = []

        c = ''
        for i in range(len(searchWord)):
            c += searchWord[i]
            idx = bs(c)
            tmp = []
            for el in range(idx, min(idx+3, len(products))):
                if products[el].startswith(c):
                    tmp.append(products[el])

            ans.append(tmp)

        return ans
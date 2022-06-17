class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        major = minor = False
        v1 = v2 = False
        arr = []
        version1_list = [int(x) for x in version1.split('.')]
        version2_list = [int(x) for x in version2.split('.')]

        if len(version1_list) < len(version2_list):
            v1 = True
        elif len(version2_list) < len(version1_list):
            v2 = True

        diff = abs(len(version1_list) - len(version2_list))

        if v1:
            while diff > 0:
                version1_list.append(0)
                diff -= 1
        elif v2:
            while diff > 0:
                version2_list.append(0)
                diff -= 1

        arr.append(version1_list)
        arr.append(version2_list)

        left = 0
        right = 1

        while right < len(arr):
            for i in range(len(arr[left])):
                # if len(str(arr[left][i])) < len(str(arr[right][i])):
                #     arr[left][i] = int(str(arr[left][i])+'0')
                # elif len(str(arr[left][i]))  > len(str(arr[right][i])):
                #     arr[right][i] = int(str(arr[right][i])+'0')
                if arr[left][i] > arr[right][i]:
                    major = True
                    break
                elif arr[left][i] < arr[right][i]:
                    minor = True
                    break
                else:
                    continue
            left += 1
            right += 1

        if not(major) and not(minor):
            return 0
        else:
            if major:
                return 1
            else:
                return -1
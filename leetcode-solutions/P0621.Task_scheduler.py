class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)

        if n == 0:
            return len(tasks)

        sorted_list = sorted(counter.values())
        mx_cnt = sorted_list.pop()

        idle_space = (mx_cnt - 1) * n

        while sorted_list:
            if idle_space <= 0:
                return len(tasks)
            idle_space -= min(sorted_list.pop(), mx_cnt - 1)

        return idle_space + len(tasks)

# Method 2

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)

        lst = []

        for v in mp.values():
            lst.append(-v)

        t = 0
        heapq.heapify(lst)
        q = deque()

        while lst or q:
            t += 1
            if lst:
                el = heapq.heappop(lst)
                c = 1 + el
                if c: q.append([c, t + n])
            if q and q[0][1] == t:
                heapq.heappush(lst, q.popleft()[0])

        return t
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

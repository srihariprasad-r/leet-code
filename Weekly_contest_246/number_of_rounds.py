class Solution(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        startTime_hr, startTime_min = int(startTime.split(':')[0]), int(startTime.split(':')[1])
        finishTime_hr, finishTime_min = int(finishTime.split(':')[0]), int(finishTime.split(':')[1])

        stTime  = 60 * startTime_hr + startTime_min
        ftTime = 60 * finishTime_hr + finishTime_min

        if stTime > ftTime:
            ftTime += 60 *24

        return max(0, ftTime//15 - (stTime+14)//15)
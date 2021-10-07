"""

https://www.lintcode.com/problem/919/description




"""

import heapq
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x : x.start)
        counter = 0
        minHeap = []
        for interval in intervals:
            heapq.heappush(minHeap, interval.end)

            if interval.start < minHeap[0]:
                counter+=1
            else:
                heapq.heappop(minHeap)
        return counter

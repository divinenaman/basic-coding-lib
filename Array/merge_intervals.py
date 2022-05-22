# https://www.interviewbit.com/problems/merge-intervals/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):

        prefix = [new_interval]
        for i, it in enumerate(intervals):
            if prefix[-1].end < it.start:
                return prefix + intervals[i:]

            elif prefix[-1].start > it.end:
                temp = prefix[-1]
                prefix[-1] = it
                prefix.append(temp)
            
            else:
                new_interval = Interval(min(prefix[-1].start, it.start), max(prefix[-1].end, it.end)) 
                prefix[-1] = (new_interval)

        return prefix  

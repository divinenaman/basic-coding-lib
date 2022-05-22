# https://www.interviewbit.com/problems/merge-overlapping-intervals/



# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# O(Nlog(N)) : sort and merge intervals
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):

        def cal(intervals):
            prefix = [intervals[0]]
            for j, i in enumerate(intervals[1:]):
                if max(prefix[-1].start, i.start) > min(prefix[-1].end, i.end):
                    if prefix[-1].end < i.start:
                        prefix.append(i)
                    else:
                        temp = prefix[-1]
                        prefix[-1] = i
                        prefix.append(temp) 
                else:
                    prefix[-1].start = min(prefix[-1].start, i.start)
                    prefix[-1].end = max(prefix[-1].end, i.end)

            return prefix

        intervals.sort(key=lambda y: y.start)    
        prefix = cal(intervals)    
        return prefix


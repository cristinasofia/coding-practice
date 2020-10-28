def merge(intervals):
    merge = []
    intervals.sort(key=lambda x:x[0])

    return merge

# Given a collection of intervals, merge all overlapping intervals.

intervals = [[1,3],[2,6],[8,10],[15,18]]
# [[1,6],[8,10],[15,18]]
print(merge(intervals))
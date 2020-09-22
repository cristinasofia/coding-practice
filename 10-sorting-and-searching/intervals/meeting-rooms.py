class Solution(object):
    def merge(self, intervals):
        merge = []
        intervals.sort(key=lambda x:x[0])


        return merge

    def meetings1(self, intervals):

    def meetings2(self, intervals):


def main():
    obj = Solution()
    # Given a collection of intervals, merge all overlapping intervals.

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # [[1,6],[8,10],[15,18]]
    print(obj.merge(intervals))

    # Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
    # determine if a person could attend all meetings.

    m1 = [[0,30],[5,10],[15,20]]

    print(obj.meetings1(m1))

    # Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
    # find the minimum number of conference rooms required.

    m2 = [[0,30],[5,10],[15,20]]

    print(obj.meetings2(m2))

    

if __name__ == "__main__":
    main()
# 252 https://leetcode.com/problems/meeting-rooms/submissions/

def canAttendMeetings(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: bool
    """

    start = []
    end = []
    for i in intervals:
        start.append(i[0])
        end.append(i[1])
    
    start.sort()
    end.sort()
    
    for i in range(1, len(intervals)):
        if start[i] < end[i-1]:
            return False
            
    return True

# 253 https://leetcode.com/problems/meeting-rooms-ii/

def minMeetingRooms(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
            
    start = []
    end = []
    for i in intervals:
        start.append(i[0])
        end.append(i[1])
    
    start.sort()
    end.sort()
    
    rooms = 0
    j = 0
    for i in range(len(start)):
        if start[i] < end[j]:
            rooms += 1
        else:
            j += 1

    return rooms

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# determine if a person could attend all meetings.

m1 = [[0,30],[5,10],[15,20]]

print(canAttendMeetings(m1))

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# find the minimum number of conference rooms required.

m2 = [[0,30],[5,10],[15,20]]

print(minMeetingRooms(m2))

 
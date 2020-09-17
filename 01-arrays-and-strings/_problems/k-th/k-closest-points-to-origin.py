class Solution(object):
    def by_sorting(self, points, K):
        points.sort(key = lambda p: p[0]**2 + p[1]**2)
        return points[:K]
    
    def by_minheap(self, points, K):
        import heapq
        return heapq.nsmallest(K, points, key=lambda p: p[0]**2 + p[1]**2)
    
    def by_quickselect(self, points, K):
        import math
        def partition(l, r):
            low = l
            while l < r:
                x = math.sqrt(pow(int(points[l][0]),2) + pow(int(points[l][1]),2))
                y = math.sqrt(pow(int(points[r][0]),2) + pow(int(points[r][1]),2))
                if x < y:
                    points[l], points[low] = points[low], points[l]
                    low += 1
                l += 1
            
            points[r], points[low] = points[low], points[r]
            return low
            
        def select(l, r):
            
            pos = partition(l, r)
            if K > pos:
                # go right
                return select(pos+1,r)
            elif K < pos:
                # go left
                return select(l, pos-1)
            else:
                return points[:pos]
            
            
        return select(0, len(points)-1)


def main():
    obj = Solution()
    # We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
    # (Here, the distance between two points on a plane is the Euclidean distance.)
    # You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

    points = [[1,3],[-2,2]]
    K = 1

    print(obj.by_sorting(points, K))
    print(obj.by_minheap(points, K))
    print(obj.by_quickselect(points, K))


if __name__ == "__main__":
    main()
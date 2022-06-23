class Solution:
    def mergeIntervals(self,arr):
            
            arr.sort()

            m = []
            s = -10000
            max = -100000
            for i in range(len(arr)):
                a = arr[i]
                if a[0] > max:
                    if i != 0:
                        m.append([s,max])
                    max = a[1]
                    s = a[0]
                else:
                    if a[1] >= max:
                        max = a[1]
                #print(m)

            if max != -100000 and [s, max] not in m:
                m.append([s, max])
            print("The Merged Intervals are :", end = " ")
            for i in range(len(m)):
                # print(m[i], end = " ")
                return m

solution = Solution()
arr = [[1,3],[2,6],[8,10],[15,18]]
print(solution.mergeIntervals(arr))

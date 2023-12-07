'''
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

'''



# def checkStraightLine(arr):
#     if len(arr) < 2: return True
#     for i in range(2, len(arr)):
#         y = arr[i][0] + 2
#         if y != arr[i][1]:
#             return False
#         else:
#             return True

# arr = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]


# def checkStraightLine(arr):
#     if len(arr) < 2: return True
#     xDiff = arr[1][1] - arr[0][1]
#     yDiff = arr[1][0] - arr[0][0]
#     for i in range(2, len(arr) + 1):
#         newXDiff = 

print(702 // 26)






# print(checkStraightLine(arr))

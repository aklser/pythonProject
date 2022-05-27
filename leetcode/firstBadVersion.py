# class Solution:
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         f,e =1,n
#         mid = 0
#         while f<n:
#             mid = f+(f-d)//2
#             if isBadVersion(mid):
#                 e = mid
#             else:
#                 f = mid + 1
#         return e
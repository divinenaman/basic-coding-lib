class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        g = 0
        num = 0

        for i in A:
            #print(i, i^g)
            if i ^ g == 0:
                g = 1 ^ g
                num += 1

        return num


o = Solution()

A = [1, 1, 0, 0, 1, 1, 0, 0, 1]

print(o.bulbs(A))

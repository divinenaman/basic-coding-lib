# https://www.interviewbit.com/problems/partitions/

# 2^log(n) solutions, inefficient, missed the key point to solve the problem ie, x1 = x2 = x3 => x1 = x2 = x3 = (x1+x2+x3)/3
class Solution1:
    def solve(self, A, B):
        def cal(sm, idx, partition):
            count = 0
            if idx < A:
                if partition + 1 < 3:
                    temp = sm.copy()
                    temp[partition + 1] += B[idx]
                    ans = cal(temp, idx+1, partition + 1)
                    count += ans

                if partition > -1:
                    temp = sm.copy()
                    temp[partition] += B[idx]
                    ans = cal(temp, idx+1, partition)    
                    count += ans    
            
            if sm[0] == sm[1] and sm[1] == sm[2] and partition == 2 and idx == A:
                return count + 1
            else:
                return count

        c = cal([0,0,0], 0, -1)

        return c

# O(N)     
class Solution2:
    def solve(self, A, B):

        sum_total = sum(B)
        
        if sum_total % 3 != 0:
            return 0

        s = sum_total // 3

        temp = 0
        pre = 0
        suffix = [0] * A

        # suffix sum of total required value (s) spotted from range i to n 
        for i in range(A-1, -1, -1):
            temp += B[i]
            suffix[i] = pre

            if temp == s:
                suffix[i] += 1
                pre += 1

        temp = 0
        count = 0
        for i in range(A-2):
            temp += B[i] 

            if temp == s:
                # i + 2 => minimum condition for the middle subarray to atleast have length 1
                count += suffix[i+2]
        
        return count

# O(N): fastest implementation but doesnt work if sum == 0
class Solution3:
    def solve(self, A, B):

        sum_total = sum(B)
        
        if sum_total % 3 != 0:
            return 0

        s = sum_total // 3
        s_twice = 2 * s

        prefix = 0
        temp = 0
        count = 0
        for i in range(A-1):
            temp += B[i] 
            
            if temp == s:
                prefix += 1
                
            if temp == s_twice:
                count += prefix

        return count
        
A1 = 5
B1 = [ 1, 2, 3, 0, 3 ]

A2 = 4
B2 = [ 0, 1, -1, 0 ]

o1 = Solution1()
o2 = Solution2()
o3 = Solution3()

print(o3.solve(A2,B2))
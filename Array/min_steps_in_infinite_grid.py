# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/


# bad solution, made simple problem complex
class Solution_1:
    def coverPoints(self, A, B):
        steps = 0
        
        if len(A) <= 1:
            return 0

        curr_point = (A[0], B[0])
        next_point = (A[1], B[1])
        idx = 2

        while next_point != None:    
                
            dir_x = next_point[0] - curr_point[0]
            dir_y = next_point[1] - curr_point[1] 
            
            if dir_x == 0 and dir_y == 0:
                if idx < len(A):
                    next_point = (A[idx], B[idx]) 
                    idx +=1
                else:
                    next_point = None

            elif dir_x == 0 or dir_y == 0:
                steps += int(abs(dir_x) + abs(dir_y))
                curr_point = next_point

            else:
                inc_x = 0
                inc_y = 0
                
                if abs(dir_x) < abs(dir_y):
                    sign_y = 1
                    if dir_y < 0:
                        sign_y = -1

                    steps += int(abs(dir_x))
                    curr_point = (curr_point[0] + dir_x, curr_point[1] +  sign_y * int(abs(dir_x)))

                else:
                    sign_x = 1
                    if dir_x < 0:
                        sign_x = -1

                    steps += int(abs(dir_y))
                    curr_point = (curr_point[0] +  sign_x * int(abs(dir_y)), curr_point[1] +  dir_y)
        
        return steps

# Optimal Solution
class Solution_2:
    def coverPoints(self, A, B):
        steps = 0
        for i in range(1, len(A)):
            curr_point = (A[i-1], B[i-1])
            next_point = (A[i], B[i])
            
            steps += max(abs(next_point[0] - curr_point[0]), abs(next_point[1] - curr_point[1]))

        return steps

A = [ -7, -13 ]
B = [ 1, -5 ]

A = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
B = [ 4, -15, -10, -3, -13, 12, 8, -8 ]

o = Solution_2()


print(o.coverPoints(A,B))
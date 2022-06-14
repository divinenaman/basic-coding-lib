class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        s = A.split(":")
        h = s[0]
        h_r = s[0][::-1]
        m = s[1]

        if h_r == m: 
            return 0
        elif int(h_r) > int(m) and int(h_r) < 60:
             return int(h_r) - int(m)
        else:
            h = str((int(h) + 1) % 24)
            if len(h) < 2:
                h = "0" + h

            return 60 - int(m) + self.solve(h + ":00")
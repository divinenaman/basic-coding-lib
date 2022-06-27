# optimal solution
class Solution1:
    def trap(self, arr):
        
        n = len(arr)
        
        l = 0
        h = n-1
        lmax = 0
        rmax = 0
        s = 0
        while l < h:
            
            if arr[l] < arr[h]:
                if lmax <= arr[l]:
                    lmax = arr[l]
                
                else:
                    s+=(lmax-arr[l])
                
                l+=1
            
            else:
                if rmax <= arr[h]:
                    rmax = arr[h]
                else:
                    s+=(rmax-arr[h])
                
                h-=1
            
        return s



# another solution can using prefix + suffix arrays
# Solution 2


# non optimal butter than brute forcer
class Solution3:
    def trap(self, arr):
        
        n = len(arr)
        
        l = 0
        h = 1
        k = (h, h)
        area = 0
        total = 0
        
        while h < n:
            
            if arr[h] < arr[l]:
                if arr[k[0]] <= arr[h]:
                    k = (h, area)        
                
                if h+1 == n:
                    total += (k[0]-l-1) * arr[k[0]] - k[1] 
                    area = 0
                    l=k[0]
                    h=k[0]+1    
                    k=(h, h)
                
                else:
                    area += arr[h]
                    h+=1
                    
            elif arr[h] >= arr[l]:
                total += (h-l-1)*min(arr[l], arr[h]) - area
                area = 0
                l=h
                h+=1
                k=(h, h)
            
        
        return total
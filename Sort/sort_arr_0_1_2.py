# move low pointer and compute m or h accordingly
class Solution1:
    def sortColors(self, arr: List[int]) -> None:
        n = len(arr)
        
        l = 0
        h = n-1
        m = n-1

        while l <= m:
            if arr[l] == 0:
                l += 1

            elif arr[l] == 2:
                while arr[h] == 2 and h > l:
                    h-=1
                
                if h <= l:
                    break
                    
                arr[l], arr[h] = arr[h], arr[l]
                h-=1
            
            elif arr[l] == 1:
                if h < m:
                    m = h

                while arr[m] == 1 and m > l:
                    m-=1
                
                if m <= l:
                    break
                
                arr[l], arr[m] = arr[m], arr[l]
                m-=1

# move mid pointer and compare its value        
class Solution2:
    def sortColors(self, arr: List[int]) -> None:
        n = len(arr)
        
        l = 0
        h = n-1
        m = 0

        while m <= h:
            if arr[m] == 0:

                if l != m:
                    arr[l], arr[m] = arr[m], arr[l]
                
                l += 1
                m += 1
            
            elif arr[m] == 2:
                if h != m:
                    arr[m], arr[h] = arr[h], arr[m]

                h-=1

            else:
                m+=1 

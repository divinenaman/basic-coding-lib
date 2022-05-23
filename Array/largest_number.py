# https://www.interviewbit.com/problems/largest-number/

# O(Nlog(N)) using merger sort and custom comparator
class Solution1:
    def largestNumber(self, A):
        # A = list(A)
        def comparator(val1, val2):
            if val1 == 0 or val2 == 0:
                return val1 > val2

            s1 = str(val1)
            s2 = str(val2)
            
            if int(s1+s2) > int(s2+s1):
                return True
            else:
                return False

        def mergeSort(arr, l, h):
            if l < h:
                mid = (l + h)//2
                
                mergeSort(arr, l, mid)
                mergeSort(arr, mid+1, h)

                temp1 = arr[l:mid+1]
                temp2 = arr[mid+1:h+1]

                i = j = 0
                c = l                
                while i < len(temp1) and j < len(temp2):
                    if comparator(temp1[i],temp2[j]) == True:
                        arr[c] = temp1[i]
                        i+=1
                    else:
                        arr[c] = temp2[j]
                        j+=1
                    c+=1
                
                while i < len(temp1):
                    arr[c] = temp1[i]
                    i+=1
                    c+=1
                
                while j < len(temp2):
                    arr[c] = temp2[j]
                    j+=1
                    c+=1
        
        mergeSort(A, 0, len(A) - 1)
        num = int("".join(list(map(str, A))))
        return num

from functools import cmp_to_key

class Solution2:
	# @param A : tuple of integers
	# @return a strings
	def largestNumber(self, A):
	    # Convert to string once, for proper comparison a+b vs b+a
	    A = map(str, A)
	    key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
	    res = ''.join(sorted(A, key= key, reverse=True))
	    # Must left trim 0, apparently
	    res = res.lstrip('0')
	    return res if res else '0'

o = Solution1()

A = [ 9, 99, 999, 9999, 9998 ]

print(o.largestNumber(A))
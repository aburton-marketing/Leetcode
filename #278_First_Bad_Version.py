# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

def firstBadVersion(n):
    if n < 3:
        for i in range(1, n):
            if isBadVersion(i) == True:
                firstBadVersion = i
                return firstBadVersion
    # Binary Search setup
    high = n - 1
    low = 0
    while low <= high:
        firstBadVersion = None
        mid = (low + high) // 2
        # ((M - 1), (M), (M + 1)) -> Sequence to help us determine if we should move forward. FFT(found at mid + 1, FTT(found at mid), FFF(none, increase low to mid + 1)

        # FFT
        if isBadVersion(mid - 1) == False and isBadVersion(mid) == False and isBadVersion(mid + 1) == True:         
            print(mid - 1, mid, mid + 1, "FFT")
            firstBadVersion = mid + 1
            break
        # FTT 
        elif isBadVersion(mid - 1) == False and isBadVersion(mid) == True and isBadVersion(mid + 1) == True:
            print(mid - 1, mid, mid + 1, "FTT")
            firstBadVersion = mid
            break
        elif isBadVersion(mid - 1) == True and isBadVersion(mid) == True and isBadVersion(mid + 1) == True:
            print(mid - 1, mid, mid + 1)
            high = mid - 1
        # FFF 
        elif isBadVersion(mid - 1) == False and isBadVersion(mid) == False and isBadVersion(mid + 1) == False:          
            print(mid - 1, mid, mid + 1)
            low = mid + 1
        else:
            print(mid - 1, mid, mid + 1)
            return False 
    return firstBadVersion          







def binary_search(A, key):
    low = 0
    high = len(A)-1   
    while low <= high:
        mid = (low+high)//2
        if key == A[mid]:
            print(mid)
            return True
        elif key < A[mid]:
            high = mid-1
        else:
            low = mid +1
    else:
        return False


A = [1,2,3,4,5,6]
key = 8

print(binary_search(A, key))
            
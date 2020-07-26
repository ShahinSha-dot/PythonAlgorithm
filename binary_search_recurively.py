def binary_search(A, key, low, high):
    while low<= len(A)-1:
        mid = (low+high)//2
        if key == A[mid]:
            return True
            print(mid)
        elif key < A[mid]:
            return binary_search(A, key, low, mid-1)
        else:
            return binary_search(A, key, mid+1, high)
    else:
        return False

A = [1,3,4,5,7]
key = 4
low = 0
high = len(A)-1

print(binary_search(A, key, low, high))

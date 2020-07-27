"""This program check whether the provided integer can be found by adding
integer in the provided list"""

def tns(array):
    array.sort()
    targetsum = int(input('enter target sum'))
    left = 0
    right = len(array)-1
    while left < right:
        currentsum = array[left] + array[right]
        if currentsum == targetsum:
            return [array[left], array[right]]
        elif currentsum < targetsum:
            left += 1
        elif currentsum > targetsum:
            right -= 1
    return []

#code below







#this will take O(nlog(n)) time and O(1) constant space    
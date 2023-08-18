# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# eg:  [1,8,6,2,5,4,8,3,7]==49

## Brute force approach


## Two pointer approach
def findContainerWithMostWater(array):
    left=0
    right=len(array)-1
    maxArea=0
    while(left<right):
        width=right-left
        height=min(array[left],array[right])
        area=width*height
        maxArea=max(maxArea,area)
        if(array[left]<array[right]):
            left+=1
        elif(array[left]>array[right]):
            right-=1
        else:
            left+=1
            right-=1

    print("Largest Area",maxArea)

findContainerWithMostWater([1,8,6,2,5,4,8,3,7])
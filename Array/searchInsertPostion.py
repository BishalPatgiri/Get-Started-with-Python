# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def searchInsertPosition(nums,target):
    if(nums.index(target)):
        return nums.index(target)
    else:
        global val
        val=0
        for i in range(0,len(nums)-1):
            if(nums[i]<target):
              val=i;
        return val+1
    
print("Inserted Position: ",searchInsertPosition([1,3,5,6],5))

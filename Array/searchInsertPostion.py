# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def searchInsertPosition(nums,target):
    try:
        if(nums.index(target)):
           return nums.index(target);
        
    except:
        global val
        val=0;
        for i in range(0,len(nums)-1):
            if(nums[i]<target):
              val=i;
        return val+1

print("Inserted Position: ",searchInsertPosition([1,3,5,6],5))
print("Inserted Position: ",searchInsertPosition([1,3,5,6],2))


# Advance Algorith with log(n) complexity
def searchInsertPosition(nums,target):
    left=0
    right=len(nums)-1
    lastVisited=0
    while(left<right):
        if nums[left]==target:
            return left 
        elif nums[right]==target:
            return right
        else:
            sum= round((left+right)/2)
            if lastVisited==sum:
                return right
            if nums[sum]==target:
                return sum
            elif nums[sum]<target:
                left=sum
            elif nums[sum]>target:
                right=sum
            lastVisited=sum
        
          
print("Inserted Position: ",searchInsertPosition([1,3,5,6],5))
print("Inserted Position: ",searchInsertPosition([1,3,5,6],2))
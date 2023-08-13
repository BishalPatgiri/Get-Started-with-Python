# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

index=0
target=10
inputArray=[2,3,5,8,9]

## Brute force approach
def findTwoSum():
    global index
    global output
    output=[]
    for i in range(0,len(inputArray)):
       for j in range(i+1,len(inputArray)):
            if((inputArray[i]+inputArray[j])==target):
                output.append(i)
                output.append(j) # output=[i,j]
                break # return
findTwoSum()
print("Brute force output:",output)

## Hash Map approach

def findTwoSum():
    global index
    hashMap={}
    for i in range(0,len(inputArray)):
      reminder=target-inputArray[i]
      if reminder in hashMap:
        return [hashMap[reminder],i]
      else:
        hashMap[reminder]=i


findTwoSum()
print("Hash Map output:",output)
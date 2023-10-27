# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

# Brute-force approach 
def mergeArr(num1,num2):
    if num1[0]>num2[0]:
        for i in num2:
            num1.add(i)
    return num1

print(mergeArr([1,2,3,0,0,0], [2,5,6]))
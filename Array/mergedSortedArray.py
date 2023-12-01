# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

# Brute-force approach 
def mergeArr(num1,num2):
    result=[]
    i=0
    j=0
    while i!=len(num1):
        if(num1[i] and num2[j] and num1[i]>num2[j]):
            result.append(num1[1])
            i+=1;
        elif(num2[j] and num2[j]>num1[i]):
            result.append(num2[j])
            j+=1;
        elif(num1[i] and num2[j] and num2[j]==num1[i]):
            result.append(num1[i])
            result.append(num2[j])
            i+=1
            j+=1
        
print(mergeArr([1,2,3,0,0,0], [2,5,6]))
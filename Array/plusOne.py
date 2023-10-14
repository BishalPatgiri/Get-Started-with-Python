# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# digits = [1,2,3] ,[9]

def plusOne(digits):
    joinOutPut=""
    for i in digits:
        joinOutPut=f"{joinOutPut}{i}"

    joinOutPut=int(joinOutPut)+1;
    joinOutPut=str(joinOutPut);
    outputArray=[]
    for j in joinOutPut:
        outputArray.append(int(j))
    print(f"Output: {outputArray}");

plusOne([1,2,3])
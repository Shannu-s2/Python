# Left and Right Sum Differences

# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.
# Where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return the array answer.

 

# Example 1:

# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
# Example 2:

# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0]

n=int(input("enter no of elements in the list"))

lis=[]

for i in range(n):
    ele=int(input("enter a number"))
    lis+=[ele,]


left=[0]
right=[0]

sum=0


for i in range(n-1):
    sum+=lis[i]
    left+=[sum,]

sum=0

print(left)

for i in range(n-1,0,-1):
    sum+=lis[i]
    right+=[sum,]
print(right)

new_lis=[]

for i in range(n):
    diff=left[i] - right[n-i-1]
    if (diff < 0):
        diff*=-1
        new_lis+=[diff,]
    else:
        new_lis+=[diff,]


print(new_lis)
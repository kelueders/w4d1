# Check if Number and its Double and Halve exists
# Given an array arr of integers, check if there exists two integers N and M
# such that either N is the double of M (i.e., N = 2 * M) and M is the double of N (i.e., M = 2 * N).
# Example:
# Input: arr = [2, 4, 6, 8]
# Output: true
# Explanation: N = 4 is the double of M = 2, that is, 4 = 2 * 2 and N = 4 is the half of M = 8.
# Example:
# Input: arr = [1, 2, 3, 4]
# Output: true
# Explanation: N = 2 is the double of M = 1, that is, 2 = 2 * 1 and N = 2 is the half of M = 4.
# Example:
# Input: arr = [3, 1, 7, 11]
# Output: false
# Explanation: In this case, there does not exist N and M such that N = 2 * M or M = 2 * N.


# input: array
# output: boolean
# for loop to go through each number in the array to check if the next number is double or half of the current number
# if x * 2 or x /2 is in the array, then True

def double_half(arr):
    for i in range(len(arr)):
        if (arr[i] * 2) in arr and (arr[i] / 2) in arr:
            return True
    return False
        
arr = [1, 2, 3, 5]

print(double_half(arr))


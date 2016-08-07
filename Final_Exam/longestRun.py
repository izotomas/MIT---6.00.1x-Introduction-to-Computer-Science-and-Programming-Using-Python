'''
Write a function called longestRun, which takes as a parameter a list of integers 
named L (assume L is not empty). This function returns the length of the longest run 
of monotonically increasing numbers occurring in L. A run of monotonically increasing 
numbers means that a number at position k+1 in the sequence is either greater than or 
equal to the number at position k in the sequence.

For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the 
value 5 because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].


You may find it useful to use the function getSublists as defined above but you do not have 
to use this function. If you do use getSublists, the graders will use our implementation 
for getSublists. In the box for this problem, only paste the definition for the function longestRun.
'''

def longestRun(L):
    longest = 1
    tmp = 1
    for i in range(len(L) - 1):
        # print L[i]
        if L[i] <= L[i+1]:
            tmp += 1
        else:
            if tmp > longest:
                longest = tmp
            tmp = 1
        if tmp > longest:
            longest = tmp
    return longest

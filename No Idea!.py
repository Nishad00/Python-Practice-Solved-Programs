# There is an array of integers. There are also disjoint sets, and , each containing integers. You like all the integers in set and dislike all the integers in set . Your initial happiness is . For each integer in the array, if , you add to your happiness. If , you add

# to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since
# and

# are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Constraints


# Input Format

# The first line contains integers
# and separated by a space.
# The second line contains integers, the elements of the array.
# The third and fourth lines contain integers, and

# , respectively.

# Output Format

# Output a single integer, your total happiness.

# Sample Input

# 3 2
# 1 5 3
# 3 1
# 5 7

# Sample Output

# 1

# Explanation

# You gain
# unit of happiness for elements and in set . You lose unit for in set . The element in set

# does not exist in the array so it is not included in the calculation.

# Hence, the total happiness is
# .




















# happiness = 0
# list1 = []
# list2 = []
# n,m = input().split()
# narray = input().split()
# A = input().split()
# B = input().split()
# for i in narray:
#     if i in A:
#         happiness += 1
#     if i in B:
#         happiness -= 1  
# print(happiness)

n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))



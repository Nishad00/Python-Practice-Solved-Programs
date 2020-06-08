import itertools  

def merge_list(list1, list2):
    merged_data=""
    
    l1 = len(list1)
    l2 = len(list2)
   
    for i, j in zip(range(0,len(list1)),range(len(list1)-1,-1,-1)):
        a = list1[i]
        b = list2[j]
        if a is None:
            a = ""
        if b is None:
            b = ""
            
        merged_data += a + b + " "
    
    return merged_data.strip()

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)






# Question
# Submission
# Given two lists, both having String elements, write a python program using python lists to create a new string as per the rule given below:
# The first element in list1 should be merged with last element in list2, second element in list1 should be merged with second last element in list2 and so on. If an element in list1/list2 is None, then the corresponding element in the other list should be kept as it is in the merged list.

# Sample Input	Expected Output
# list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
# list2=['y','tor','e','eps','ay',None,'le','n']	“An apple a day keeps the doctor away”
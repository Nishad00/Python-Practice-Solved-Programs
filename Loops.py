# Task
# Read an integer . For all non-negative integers , print . See the sample for details. 

list1 = []
j = 1
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n-1):
        list1.append(j)
        j+=2
    
    k = 0
    for i in range(0,n):
        print k
        if i == n-1:
            break
        else:
            k += list1[i]


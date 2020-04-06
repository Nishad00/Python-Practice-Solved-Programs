import re

handler = open("regex_sum_414355.txt",'r')
total_sum = 0
sum = 0
list1 = list()
for lines in handler:
    data = re.findall('[0-9]+',lines)
    if len(data) < 1 : continue
    for i in data:
        total_sum = total_sum + int(i) 
print(total_sum)



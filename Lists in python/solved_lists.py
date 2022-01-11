# 1)a) Sum of elements in a list
def sum(lst):
    sum = 0
    for number in lst:
        sum+=number
    return mul

# 1)b) Mul of elements in a list
def mul(lst):
    mul = 1
    for number in lst:
        mul*= number

# 1)c) Largest and smallest element in a list
min(lst)
max(lst)
# 1)d) To check if list is empty or not
def empty_list_check(lst):
    if len(lst)>0:
        True
    else:
        False
# or
def empty_list_check(lst):
    return len(lst)>0

# 1)e) To clone or copy a list
l1 = []
l2 = []
for element in l1:
    l2.append(element)
# or
l2 = l1[:]

# 1)f)To concatenate 2 lists
for element in l1:
    l2.append(element)
# or
l1.extend(l2)
# or
l1+=l2
# or
l2[:0]= l1

# 1)g)To return a list of multiplication of each number of list1 with each number of list 2 given that len of both lists is same.
def multiply(l1,l2):
    l3 = []
    for i in range(len(l1)):
        x = l1[i]*l2[i]
        l3.append(x)
    return l3
# or
def mul(l1,l2):
    return[l1[i]*l2[i] for i in range(len(l1))]
# or
def mul(l1,l2):
    return[i*j for i,j in zip(l1,l2)]

# 1)h) To access the index of a list
print(l1.index())
# 1)i) Unpacking a list(splitting objects using variables)
colors = [['black','#000000'],['blue', '#0000FF'],['white', '#FFFFFF']]
black,blue,white = colors

# 2. Python program to remove duplicates from a list
def remove_duplicates(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
# or
def remove_duplicates(lst):
    l2=[]
    [l2.append(i) for i in l1 if i not in l2]
# or
from collections import OrderedDict
x = list(OrderedDict.fromkeys(l1))

# 3. Program to print a list of words whose length is greater than n
def greater_then_n(lst,n):
    l = []
    [l.append(i) for i in lst if len(i)>n]

# 4. Write a program to count the number of strings
#    where the string length is 2 or more and
#    the first and last character are same from a given list of strings.
def str_counter(lst):
    ctr = 0
    for i in lst:
        if len(i)>=2 and i[0:]==i[-1]:
            ctr+=1

#5. Write a function that takes two lists and returns True if they have at least one common member.
def common_member(lst1, lst2):
    result = False
    for i in lst1:
        if i in lst2:
            result = True
    return result

# 6. Write a program to find common items from two lists.
def common_member(lst1, lst2):
    result_list = []
    for i in lst1:
        if i in lst2:
            result_list.append(i)
    return result_list

# or

def common_member(lst1, lst2):
    result_list = []
    [result_list.append(i) for i in lst1 if i in lst2]

# 7. Write a program to get a list, sorted in increasing order by the last element in each tuple
#     from a given list of non-empty tuples.
#     Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#     Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#     a) Find the min element
#     b) Find the max element
def sec_val(val):
    return val[-1]
def sort_list(lst):
    return sorted(lst, key=sec_val)
    return lst.sort(key=sec_val) #using.sort method
# or
def sort_list(lst):
    return sorted(lst, key=lambda val:val[-1])
    return lst.sort(key=lambda val:val[-1])  # using.sort method

# 8. Write a program to count the number of same elements in a list and return a list of tuples
#    where tuple must be(value, count)

def element_count(lst):
    result_lst = []
    for i in lst:
        result_lst.append((i,lst.count(i)))
    return list(set(result_lst))

# 9. Write a program to count the number of elements in a list within a specified range.

def count(lst,max,min):
    ctr = 0
    for i in lst:
        if max>=i>=min:
            ctr+=1
    return ctr

# 10. Write a program to convert a list of multiple integers into a single largest integer possible.
#     Sample list: [11, 50, 33]
#     Expected Output: 503311

def max_num(list):
    s = ''
    for i in sorted(list, reverse=True):
        s+=str(i)
    return int(s)

# 11. Write a Python program to find missing and additional values in two lists.
def missing(lst1,lst2):
    print("Missing Elements from list1:", ",".join(set(lst1).difference(lst2)))
# or

def additional(lst1,lst2):
    print("Missing Elements from list1:", ",".join(set(lst2).difference(lst1)))
# 12. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
#     Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
#     Expected Output: [10, 11, 12]
def max_sum(list):
    l = []
    for i in list:
        l.append(sum(i))
    x = l.index(max(i))
    return list[x]
# or

def max_sum(list):
    return max(list, key = lambda lst:sum(lst))


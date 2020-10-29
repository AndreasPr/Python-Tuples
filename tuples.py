#Tuples are a collection data type, ordered, immutable and they are the same as the lists but the main difference is that once are created,
#  they cannot be changed, allows duplicate elements

mytuple1 = ("Andreas", 90, "NY") #parenthesis is optional
print(mytuple1)

# -----------------Create Tuple from iterate e.g. List-------------------
mytuple2 = tuple(["John", 56, "CO"])
print(mytuple2)

# ----------------Access Elements--------------------
element = mytuple2[2]
print(element)

#And negative index
element = mytuple2[-2]
print(element)

#--------------Iterate Tuple--------------
for i in mytuple2:
    print(i)

#-----------------Check if exist an element in tuple-----------
if "John" in mytuple2:
    print("Yes")
else:
    print("No")

#----------------Length of the Tuple------------------
mytuple3 = ('g', 'h', 'h', 'o', 't', 'o')

print("Length:", len(mytuple3))

#------------- Count specific elements of the tuple --------------
print(mytuple3.count('h'))

#-----------------Index of an element in tuple (return the first which is found)----------------
print(mytuple3.index('h'))

#----------------Convert a tuple to list vice versa
my_list1 = list(mytuple3)
print(my_list1)

mytuple4 = tuple(my_list1)
print(mytuple4)

#----------------Slicing------------------
a = (1,2,3,4,5,6,7)

b = a[2:5]
print(b)

# With steps, take every second element
b = a[::2]
print(b)

# Reverse a tuple
b = a[::-1]
print(b)


#------------------------Unpacking-------------------
mytuple5 = "Andreas", "TX", 23

name, state, age = mytuple5
print(name)
print(state)
print(age)


# Trick to unpack multiple elements - The multiple elements would be inserted to a List
mytuple6 = (1,2,3,4,5,6,7,8)

x1, *x2, x3 = mytuple6

print(x1) # 1
print(x3) # 8
print(x2) #[2,3,4,5,6,7]

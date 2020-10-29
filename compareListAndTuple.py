import sys
import timeit

sample_list = [0,4,5,"Andreas",7,True]
sample_tuple = (0,4,5,"Andreas",7,True)

print(sys.getsizeof(sample_list), "bytes") #112 bytes
print(sys.getsizeof(sample_tuple), "bytes") #96 bytes

# Create a list & Tuple 100000000 times and see the time performance
print(timeit.timeit(stmt="[0,1,2,3,4]", number=10000)) #0.000723399999999999 time of the List
print(timeit.timeit(stmt="(0,1,2,3,4)", number=10000)) #0.0001989999999999978 time of the Tuple


# So, Tuple is more efficient than List, especially with large data
"""
-------------------------------------------------------
[Assignment 5, Task 2]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-22"
-------------------------------------------------------
"""

from Sorted_List_array import Sorted_List
from Movie_utilities import read_movies


fh = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fh)


target = Sorted_List()

source1 = Sorted_List()

source2 = Sorted_List()

i = 1

target.insert(movies[0])
target.insert(movies[1])
target.insert(movies[2])


value = target[i] #get_item

print()
print("Finding item (get_item)")
print()
print(value)

target.insert(movies[0])
target.insert(movies[1])
target.insert(movies[2])
target.insert(movies[1])
target.insert(movies[2])
target.insert(movies[3])


target.clean()

print()
print("Cleaning Check")

for x in target:
    print()
    print(x)
    

source1.insert(movies[5])
source2.insert(movies[5])
    
target.intersection(source1, source2)

print()
print("Intersection check") #will be unchanged because there is not intersection

for x in target:
    print()
    print(x)
    
n = target.index(movies[5])

print()
print("Index check") #will be unchanged because there is not intersection
print()
print(n)

    
b = target.is_identical(source1)


print()
print("Indenitcal check")
print()

if b == True:
    print("True")
else:
    print("False")
    

print()
value = target.remove_front()

print("Remove Front Check")

for x in target:
    print()
    print(x)

key = movies[2]

target.remove_many(key)

print()
print("Remove Many Check")

for x in target:
    print()
    print(x)
    
    
target1, target2 = target.split()

print()
print("Split Check")

print()

print("Split1")

for x in target1:
    print()
    print(x)
    
    
print()

print("Split2")

for x in target2:
    print()
    print(x)
    
print()

target.insert(movies[1])
target.insert(movies[2])
target.insert(movies[3])
target.insert(movies[4])

target3, target4 = target.split_alt()

print("Alt Split Check")

print()

print("Split1")

for x in target3:
    print()
    print(x)

print()

print("Split2")

for x in target4:
    print()
    print(x)
    
    
source1.insert(movies[7])

target.union(source1, source2) #source2 list is currently empty, source 1 had 1 element

print()
print("Union Check") 

for x in target:
    print()
    print(x)

key = movies[7]

value = target.find(key)

print()
print("Find Check") 
print()
print(value)

n = target.count(key)

print()
print("Count Check") 
print()
print(n)

value = target.remove(key)

print()
print("Remove Check") 
print()
print(value)

value = target.peek()

print()
print("Peek Check") 
print()
print(value)

value = target.min()

print()
print("Min Check")
print()
print(value)

value = target.max()

print()
print("Max Check")
print()
print(value)

print()
print("Contain Check")
print()

b = key in target

if b == True:
    print("Yes")
else:
    print("No")

target.insert(movies[0])
target.insert(movies[1])

key = movies[2]
    
target1, target2 = target.split_key(key) #everything should be in split 1 cuz zulu is last in the key

print("Key Split Check")

print()

print("Split 1")

for x in target1:
    print()
    print(x)

print()

print("Split 2")

for x in target2:
    print()
    print(x)
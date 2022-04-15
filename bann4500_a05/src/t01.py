"""
-------------------------------------------------------
[Assignment 5, Task 1]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-22"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Movie_utilities import read_movies


fh = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fh)


target = List()

target.append(movies[0])

print("Append check")

for x in target:
    print()
    print(x)

source1 = List()

source2 = List()

source1.append(movies[1])

source2.append(movies[2])

target.combine(source1, source2)

print()
print("Combine test")
for x in target:
    print()
    print(x)

i = 1

value = target[i] #get_item

print()
print("Finding item (get_item)")
print()
print(value)

target.append(movies[1])

target.append(movies[2])

target.clean()

print()
print("Cleaning Check")

for x in target:
    print()
    print(x)
    
    
    
target.intersection(source1, source2)

print()
print("Intersection check") #will be unchanged because there is not intersection

for x in target:
    print()
    print(x)

    
b = target.is_identical(source1)


print()
print("Indenitcal check")
print()

if b == True:
    print("True")
else:
    print("False")
    
    
print()

target.prepend(movies[5])

print("Prepend Check")

for x in target:
    print()
    print(x)

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

target.append(movies[1])
target.append(movies[2])
target.append(movies[3])
target.append(movies[4])

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
    
    
source1.append(movies[7])

target.union(source1, source2) #source list is currently empty

print()
print("Union Check") 

for x in target:
    print()
    print(x)



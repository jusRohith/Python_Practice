#! List Datastructure
#! List Properties
"""If you want to represent group of individual objects into a single entity then 
    we should go for collections """
#! List, Tuple, Set, FrozenSet, Dict, Bytes, BytesArray
# ? When to use List
# todo When you want to store Duplicate objects and Insertion order must be required.
# * Insertion Order Preserved
# * Duplicates allowed
# * Heterogenous objects allowed
# * Growable in Nature (Dynamic)
# * []

# ? How to create List Object
#! There are few ways to create the list
# * 1.To create empty list object using []
l = []
print(l, type(l))
# * 2.If you know the data already
l = [10, 20, 30, 40]
print(l, type(l))
# *3 Dynamic input
l = eval(input("Enter numbers using [] :"))
# *4 create using list() function, we can create empty list and convert sequence to list
l = list()
print(l, type(l))
l = list(range(0, 11, 2))
print(l, type(l))
# *5 By using String split() function
s = "Learning python is very easy"
l = s.split()  #! split() method returns list object
print(l, type(l))

# ? How to access elements of the List
# todo There are two ways
# * Indexing
l = [10, 20, 30, 40, 50]
print(l[2])  #! 30
print(l[-1])  #! 50
print(l[40])  #! We get Index Error
# * Slice Operator
#! Slice Operator syntax l[Begin : End : Step]
# todo +ve direction => Forward Direction => Begin to End-1
# todo -ve direction => Backward Direction => Begin to End+1


l = []
for x in range(1, 101):
    if x % 10 == 0:
        l.append(x)
print(l)
l.insert(2, 45)
print(l)
l.insert(40, 110)
print(l)
l.insert(-99, 5)
print(l)

l1 = [10, 20, 30, 40, 50]
l2 = [60, 70, 80, 90, 100]
l3 = l1 + l2  #! Creates and returns new list
print("L3 : ", l3)
#! L.append() VS L.extend()
order1 = ["chicken", "mutton", "fish"]
order2 = ["KF", "KO", "RC"]
order1.extend(order2)
l1.append(order2)
print(l1)
print(order1)  #! list.extend() function modifies existing list and returns none

l1.append("Rohith")
print(l1)
order1.extend("Rohith")
print(order1)

# ? Important methods in List Datastructure
# todo To increase the size of the list
# * l.append(__object: int,/) -> None
# * l.insert(__index: SupportsIndex,__object: int,/) -> None
# * l.extend(__iterable: Iterable[int],/) -> None
# todo To decrease size/ to remove elements
# * l.remove(__value: int,/) -> None
# * l.pop(__index: SupportsIndex = -1,/) -> int
# * l.clear() -> None
# todo Ordering elements in the list
# * 1. Reverse Order:
# ? l.reverse() -> None # It wont create or return new object in the existing list only elements will be reversed
# ? reversed(l)
# * 2.Sorting Order:
# ?l.sort()-> None  To use this method list should contain only homogenous elements
# ? sorted(l) -> List
# todo Cloning of List Object
list1 = [10, 20, 30, 40]
list2 = list1[::]  #! By using slice object we can create new object copy of the object
list3 = list1.copy()  #! Copy method creates new object
print(l1 is l2)
print(l1 is l3)

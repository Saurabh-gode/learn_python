# my_list = [23, [1], 5, "Hellow"]

# my_list.insert(1,2)

# print(my_list)

# my_tuple = (1, 2, 3, 4, 5)

# print(id(my_tuple))

# my_tuple = my_tuple + (6, 7, 8)
# print(id(my_tuple))
# print(len(my_tuple))

# my_list2 = list([1,2,3,4,5])

# print(my_list2)
# my_tuple2 = tuple(my_list2)
# print(my_tuple2)

# list challenge

list = [12, 12 ,"Greg", "text", "more text", 12, 45, 12, 90, "adam", 43, 12323]

for i in range(len(list)):
    if(list[i] == "adam"):
        list[i] = list[i].upper()

print(list)


# using enumerate

# returns tuple with index and its value
for (index, value) in enumerate(list):
    if(value == "adam"):
        list[index] = value.upper()

print(list)


for item in list:
    if(item == "adam"):
        index = list.index(item)
        list[index] = item.upper()

print(list)


# using map
def to_upper(item):
    if(item == "adam"):
        return item.upper()
    return item
list = list(map(to_upper, list))
print(list)



# using lambda
list = list(map(lambda item: item.upper() if item == "adam" else item, list))
print(list)


# using list comprehension
list = [item.upper() if item == "adam" else item for item in list]
print(list)

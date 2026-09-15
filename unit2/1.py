print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")
# 1. CREATING LISTS

numbers = [10, 20, 30, 40]
mixed = ['Python', 100, 3.14, True]
print("Numbers list:", numbers)
print("Mixed list:", mixed)


# 2. ACCESSING LIST ELEMENTS

fruits = ['apple', 'banana', 'cherry', 'date']

print("First element (index 0):", fruits[0])
print("Last element (index -1):", fruits[-1])


# 3. UPDATING LISTS

items = [10, 20, 30, 40]

items[1] = 99         # Update single element
items[2:4] = [77, 88] # Update slice range

print("Updated list:", items)


# 4. DELETE LIST ELEMENTS

del_items = ['a', 'b', 'c', 'd']
del del_items[1]      # Delete element at index 1 ('b')


print("After del items[1]:", del_items)


# 5. BASIC LIST OPERATIONS

list_a = [1, 2]
list_b = [3, 4]

print("Length len():", len(list_a))
print("Concatenation (+):", list_a + list_b)
print("Repetition (*):", list_a * 3)
print("Membership (in):", 2 in list_a)


# 6. INDEXING, SLICING AND MATRICES

tech = ['C++', 'Java', 'Python', 'Go', 'Rust']
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Offset index [2]:", tech[2])
print("Negative index [-2]:", tech[-2])
print("Slicing [1:4]:", tech[1:4])
print("Matrix row 0, col 1:", matrix[0][1])


# 7. BUILT-IN FUNCTIONS

nums_func = [45, 12, 89, 3]
sample_tuple = (1, 2, 3)

print("len():", len(nums_func))
print("max():", max(nums_func))
print("min():", min(nums_func))
print("list(tuple):", list(sample_tuple))


# 8. BUILT-IN METHODS 


# append()
data = [1, 2]
data.append(3)
print("append(3):", data)

# count()
count_data = [10, 20, 10, 30, 10]
print("count(10):", count_data.count(10))

# extend()
ext_data = [1, 2]
ext_data.extend([3, 4])
print("extend([3, 4]):", ext_data)

# index()
idx_data = ['red', 'green', 'blue']
print("index('green'):", idx_data.index('green'))

# insert()
ins_data = [10, 30]
ins_data.insert(1, 20)
print("insert(1, 20):", ins_data)

# pop()
pop_data = [10, 20, 30]
popped_val = pop_data.pop()
print("pop value:", popped_val)
print("after pop():", pop_data)

# remove()
rem_data = ['apple', 'banana', 'cherry']
rem_data.remove('banana')
print("remove('banana'):", rem_data)

# reverse()
rev_data = [1, 2, 3, 4]
rev_data.reverse()
print("reverse():", rev_data)

# sort()
sort_data = [40, 10, 30, 20]
sort_data.sort()
print("sort() ascending:", sort_data)

sort_data.sort(reverse=True)
print("sort() descending:", sort_data)

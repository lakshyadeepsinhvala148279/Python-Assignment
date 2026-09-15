print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")
#Accessing Values in Tuples
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])


#Updating Tuples

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print (tup3)

#Delete Tuple Elements

tup= ('physics', 'chemistry', 1997, 2000);
print (tup)
del tup1;
print ("After deleting tup : ")
print (tup)

#Basic Tuples Operation

# 1. Length
print(len((1, 2, 3)))  

# 2. Concatenation
print((1, 2, 3) + (4, 5, 6))  
# 3. Repetition
print(("Hi!",) * 4) 

# 4. Membership
print(3 in (1, 2, 3))  

# 5. Iteration
for x in (1, 2, 3):
    print(x, end=" ")  

# Sample Tuple & Matrix
T = ('C++', 'Java', 'Python')
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# 1. Indexing
print(T[2])
print(T[-2])

# 2. Slicing
print(T[1:])
print(T[:2])
print(T[::-1])

# 3. Matrix Access
print(matrix[0])
print(matrix[1][2])

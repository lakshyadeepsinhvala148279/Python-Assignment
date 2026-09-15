#Python program to add two matrix using array and function

print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")
A = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
B = [[9, 8, 7],
[6, 5, 4],
[3, 2, 1]]
result = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
print("Resultant Matrix after addition:")
for row in result:
    print(row)

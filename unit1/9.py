#Python program to print the largest element and smallest element in an array
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")
arr = [15, 41, 77, 95, 12]

largest = arr[0]
smallest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
    if arr[i] < smallest:
        smallest = arr[i]
        
print("Largest element:", largest)
print("Smallest element:", smallest)

print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")
def demonstrate_dictionary_operations():
    print(f"Student Enrolment No: 92600565003\n")
    
    # 1. Creating a Dictionary
    student = {
        "name": "lakshyadeepsinh",
        "age": 21,
        "course": "M.Sc. CS&CL",
        "marks": 85
    }
    print("Initial Dictionary:", student)

    # 2. Accessing Values
    print("Name:", student["name"])
    print("Course (using get()):", student.get("course"))
    print("Non-existent Key (with default):", student.get("gpa", "Not Available"))

    # 3. Adding and Updating Elements
    student["age"] = 22  # Direct assignment
    student.update({"city": "Vadodara", "marks": 90})  # Batch update
    print("After Update:", student)

    # 4. Built-in Retrieval Functions
    print("Keys:", list(student.keys()))
    print("Values:", list(student.values()))
    print("Items (Key-Value pairs):", list(student.items()))

    # 5. Removing Elements
    removed_val = student.pop("marks")
    print(f"Popped 'marks': {removed_val}")

    last_item = student.popitem()  # Removes last inserted item
    print(f"Popped last item: {last_item}")
    
    del student["age"]
    print("After deleting 'age':", student)

    # 6. Copying and Clearing
    temp_dict = student.copy()
    temp_dict.clear()
    print("Cleared Dictionary:", temp_dict)

if __name__ == "__main__":
    demonstrate_dictionary_operations()

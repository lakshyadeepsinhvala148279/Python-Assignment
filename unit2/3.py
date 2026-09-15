# Student Enrollment Number: ENROLLMENT_NO_HERE
# Aim: Python program to demonstrate the use of dictionary and various functions of it.
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565003")

def main():
    # 1. Dictionary Creation
    student_info = {
        "enrollment": "92600565003",
        "name": "Lakshyadeepsinh",
        "course": "M.Sc. CS&CL",
        "semester": 1,
        "marks": {"Python": 85, "Networking": 90}
    }
    
    print("--- Original Dictionary ---")
    print(student_info)
    print()

    # 2. Accessing Elements (using key and get() method)
    print("--- Accessing Elements ---")
    print(f"Name: {student_info['name']}")
    print(f"Course (via get()): {student_info.get('course')}")
    # get() with default fallback for non-existing keys
    print(f"Grade (default fallback): {student_info.get('grade', 'Not Assigned')}")
    print()

    # 3. Dictionary Methods: keys(), values(), and items()
    print("--- Dictionary Keys, Values, and Items ---")
    print(f"Keys: {list(student_info.keys())}")
    print(f"Values: {list(student_info.values())}")
    print(f"Items (Key-Value Pairs): {list(student_info.items())}")
    print()

    # 4. Adding and Updating Elements (via key assignment & update() method)
    print("--- Updating & Adding Elements ---")
    student_info["email"] = "lucky@example.com"  # Adding new key-value
    student_info.update({"semester": 2, "city": "Vadodara"}) # Updating existing & adding new
    print(f"Updated Dictionary: {student_info}")
    print()

    # 5. setdefault() Method
    # Returns the value if key exists; otherwise inserts key with specified default value
    status = student_info.setdefault("status", "Active")
    print(f"Status (via setdefault): {status}")
    print()

    # 6. Removing Elements (pop(), popitem(), del, clear())
    print("--- Removing Elements ---")
    removed_email = student_info.pop("email")
    print(f"Popped Key 'email': {removed_email}")
    
    # Removes and returns the last inserted key-value pair
    last_item = student_info.popitem()
    print(f"Popped Last Item (popitem): {last_item}")
    
    # Delete a specific key using 'del'
    del student_info["status"]
    print(f"Dictionary after 'del': {student_info}")
    print()

    # 7. Copying a Dictionary (copy() method)
    print("--- Copying Dictionary ---")
    student_copy = student_info.copy()
    print(f"Copied Dictionary: {student_copy}")
    print()

    # 8. Clearing a Dictionary
    student_copy.clear()
    print(f"Copied Dictionary after clear(): {student_copy}")


if __name__ == "__main__":
    main()

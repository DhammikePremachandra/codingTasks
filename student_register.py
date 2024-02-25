"""
# This program allows users to register students for an exam venue by 
# getting their student IDs and storing them in a text file 
# "reg_form.txt".

# The main function asks the user to enter the number of students 
# they want to register. Then, it iterates through the range of students
# and ask the user to enter each student's ID. The entered student
# IDs are appended to string with separator and stored in 
# the "reg_form.txt" file.
# The program will create text file "reg_form.txt" containing the 
# registered student IDs.
"""
def main():
    """
    # Function to get user inputs, collects their student IDs and 
    # write it on ".txt"file.
    """
    venue = "Nottingham"
    print(f"Welcome to the{venue}exam center!")
    # Getting the number of students are goint to register 
    # as a user input. 
    students = int(input("Please enter, how many students are registering:"))
    student_ids = ""
    for _ in range(students):
        # Get the Student ID as a user input.
        student_id = input("Enter Next Student ID:").strip()
        # Collect each Student ID to the string.
        student_ids += student_id + "\n.....................................\n" 
        
    with open("reg_form.txt", "w") as file:
        """
        # Write the collected Student ID's to the file.
        """
        file.write("Student ID\n" + student_ids)

if __name__ == "__main__":
    main()

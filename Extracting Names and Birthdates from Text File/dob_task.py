"""
# Program that reads data from a text file "DOB.txt" and prints it 
# out in two different sections.

# The program reads the "DOB.txt" file, which contains 
# lines of data, there are names and birthdates.
# Each line have the format: "FirstName LastName MM DD YYYY".

# The program then extracts the names and birthdates from each line and 
# prints them out separately.
# Finally, it appends the extracted names and birthdates to the end of 
# the DOB.txt file.

# Example input in DOB.txt:
# John Doe 01 15 1985
# Jane Smith 05 20 1990

# Example output:
# Name
# John Doe
# Jane Smith

# Birthdate
# 01 15 1985
# 05 20 1990
"""
with open('DOB.txt', 'r') as file:
    """
    # Open the file in read mode and create file object.
    """
    # Read all line in the file.
    lines = file.readlines()
    name = ""
    birth_date = ""
    for line in lines:
        # Spilt the line into seperate indexes.
        name_birth_list = line.split()
        # Extract name from the first two indexes.
        name += "\n" + " ".join(name_birth_list[0:2])
        # Extract birthdate from remaining indexes.
        birth_date += "\n" + " ".join(name_birth_list[2:])
    # Output the exracted name and birthdate.
    print(f"Name{name}\n\nBirthdate{birth_date}")

    with open('DOB.txt', 'a') as file:
        """
        # Open the file in append mood and create file object.
        """
        # Write name to the file.
        file.write(f"\nName{name}\n")
        # Write birthdate to the file.
        file.write(f"\nBirthdate{birth_date}\n")

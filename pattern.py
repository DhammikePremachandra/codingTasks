"""Output of the arrow head shape star pattern."""

# Assign maximum number of stars in  a row of the pattern into variable.
max_stars_row = 5
# Range is decide  1 to 10 according to the maximum length of stars
# in a row of the pattern.
for i in range(1 ,10):
    # Untill i == 5, if statement output the first five rows of the 
    # stars pattern.
    if i <= max_stars_row:
        print("*" * i)
    # Output last 4 rows of the stars pattern when i > 5 .  
    else:
        print("*" * (10 - i)) 

"""Program that counts how many instances of a character there are in 
# a string."""
count = 0
sentence = input("Please enter your string: ").lower()
# Validate the user's input for char to count.
while True:
    character = input(
        "Please enter the character you would like to count: "
        ).lower()
    #Check if the user as entered more than 1 char.
    if len(character) > 1:
        print("You have entered more than one character. Please try again")
    # If the character is not alphabetic, need to notify user.
    elif not character.isalpha():
        print("You have entered number or symbel, Please try again")
    else:
        break

for char in range(len(sentence)):
    if character == sentence[char]:
        count += 1
print(f"The Character: {character} appeared {count} times")

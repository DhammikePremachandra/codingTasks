"""Get a sentence from user and store the user's response in a 
    variable called "str_manip"""
str_manip = input("Please Enter a Sentence: ")
# Calculate and Display the length of the entered sentence.
lenght_sentence = len(str_manip)
print(f"The length of the sentence: {lenght_sentence}")

# The last letter of the sentence.
last_letter = str_manip[-1] # Indexing method.
# Replacing every occurrence of the last_letter into the sentence.
new_sentence = str_manip.replace(last_letter, "@")
# Display the new sentence.
print(f"New sentence: {new_sentence}")

# get the last three characters.
last_three_letters = str_manip[-3:]
# Reverse the order of the last_three.
reverse_last_three = last_three_letters[::-1]
print(f"Last three characters in backwords: {reverse_last_three}") 

# Get the first three characters of the "str_manip".
first_three_letters = str_manip[:3]
# Get the last two letters of the "str_manip".
last_two_letters = str_manip[-2:]
# Creating five letter word using "first_three_letters" and 
# "last_two_letters".
five_letter_word = first_three_letters + last_two_letters
# Displaying five letter word.
print(f"Five-letter word: {five_letter_word}")

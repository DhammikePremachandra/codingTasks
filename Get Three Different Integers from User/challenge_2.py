"""Getting input the name of a user's favourite restaurent and store it.""" 
string_fav = input("Please Enter your Favourite Restaurent: ")

# Getting input the favorite number of the user and casting it into 
# integer and store the number.
int_fav = int(input("Please Enter your favourite number:  "))

# Output the results.
print(f"Your Favourite restaurent is {string_fav}")
print(f"Your Favourite number is {int_fav}")

# Casting string_fav to the integer.
string_fav_casted = int(string_fav) # This piece of code results a 
# value error becouse string_fav is a string and we cannot cast string 
# into a integer.

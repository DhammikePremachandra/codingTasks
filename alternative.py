"""
Program that reads in a string and makes each alternate 
character into an upper case character and each other
alternate character a lower case character.
"""

def alternate_char(string):
    """
    Function to alternate the case of characters in the input string.
    """
    result = " "
    for i, char in enumerate(string):
      # If the index is even, change character into upper case.
      if i % 2 == 0:
        result = "".join([result, char.upper()])
      # If the index is not even, change character into lower case.
      else:
        result = "".join([result, (char.lower())])
    return result             

def alternate_word(string):
    """
    Function to alternate the case of words in the input string.
    """    
    results = []
    # Split the input string into words.
    string_split = list(string.split())
    for j, word in enumerate(string_split):
      # If the index is even, change the word to lower case.    
      if j % 2 == 0:
        results.append(word.lower())
      # If the index is odd, change the word to upper case.
      else:
        results.append(word.upper()) 
    """Join the modified words back into a string with 
       one space between words."""
    results_joined = " ".join(results)
    return results_joined

# Getting string from user that user need to change.
string = input("Welcome to the alternative!,Please enter a string:").strip(
               ).lower()
# Output of the new string, with alternate characters.               
print(f"Modified string with alternate characters:{alternate_char(string)}")
# Output of the new string with alternate words.
print(f"Modified string with alternate words:{alternate_word(string)}")
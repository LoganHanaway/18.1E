# def must_start_with():
#     x = input("Chose a letter: ")
#     y = input("Chose another letter: ")
#     return x, y

# x = input("Chose a letter: ")
# y = input("Chose another letter: ")

# def print_upper_words(words, x, y):
#     """ This function """
#     for word in words:
#         if word == x or word == y:
#             print(word.upper())
#         # else: 
#         #     print(word.upper())    


# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], x, y)

# second attempt

def must_start_with():
    x = input("Choose a letter: ")
    y = input("Choose another letter: ")
    return x, y

def print_upper_words(words, x, y):
    """Prints words from a list that start with either 'x' or 'y', in uppercase."""
    for word in words:
        if word.startswith(x) or word.startswith(y):
            print(word.upper())

# Collect the letters 'x' and 'y' from the user
x, y = must_start_with()

# Test the function
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], x, y)



# this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
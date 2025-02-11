# Assignment 5:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    NOTE: chars variable can contain any even number of characters.
          the len() function can be used to figure out the length of a string

    Example:
    ---------------
    chars = "<[<||>]>"
    word = "mirror"
    result - should contain the following string: <[<|mirror|>]>

"""

chars = "<<[]]]" # this could be a very long string with an even length.
word = "Cool"

# Expected Result Printed: <<[Cool]]]


# Your code below:
mid_index = len(chars)
idx = int(mid_index/2)
result = chars[:idx] + word + chars[idx:]
print(result)

print(chars[:2] + chars[2:3] + word + chars[3:])



































# Solution Below:
# size = len(chars)
# idx = int(size/2) # dividing results in a float datatype.
# print(chars[:idx] + word + chars[idx:])



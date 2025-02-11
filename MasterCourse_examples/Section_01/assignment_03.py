# Assignment 3:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    перевод:

    Учитывая 2 переменные chars и word, напишите код для перемещения
    данных, содержащихся в переменной word, в точное середину
    символов, содержащихся в переменной chars, и сохраните это
    в новой переменной с именем result и напечатайте ее.


    NOTE: chars variable will contain only 4 characters

    Example:
    ---------------
    chars = "<<>>"
    word = "hello"
    result - should contain the following string: <<hello>>

"""

chars = "[[]]"
word = "Cool"

# Expected Result Printed: [[Cool]]

# Your code below:

result = chars[:2] + word + chars[2:]
print(result) # [[Cool]]

# Explanation:

# The code above uses string slicing to insert the word variable in the middle of the chars variable.
# The chars[:2] will get the first two characters of the chars variable.
# The chars[2:] will get the last two characters of the chars variable.
# The word variable is then inserted between the two parts of the chars variable using the + operator.
































# Solution Below:
# print(chars[:2] + word + chars[2:])



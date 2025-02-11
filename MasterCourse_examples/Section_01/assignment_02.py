# Assignment 2:
"""
Use of the below format() method is incorrect for what we are trying to do.
We actually have 10 small, 12 large, and 12 medium boxes.

перевод:
Использование нижеуказанного метода format() неверно для того, что мы пытаемся сделать.
У нас есть 10 маленьких, 12 больших и 12 средних коробок.
Write code to correct this:



print("We have {2} small boxes, {2} large boxes, {2} medium boxes".format(10,12,12))

"""

# Solution:
print("We have {0} small boxes, {1} large boxes, {2} medium boxes".format(10,12,12)) # We have 10 small boxes, 12 large boxes, 12 medium boxes

# Explanation:
# The format() method uses the index of the arguments to replace the placeholders in the string.















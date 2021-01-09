# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply(num1, num2):
    return num1 * num2

def multiply_by(numbers_list, multiple):
    result = []
    for each_num in numbers_list:
        result.append(each_num * multiple)

    return result

    # come back to that
    # result = map(multiply, numbers_list)

print(multiply_by([4,6,8,10], 10))


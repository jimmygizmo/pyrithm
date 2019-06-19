#! /usr/bin/env/python3
####################################################################################################

# First class functions are a feature of Python and other languages like Javascript. This means
# that functions are like any other object and can be passed as arguments and returned as return
# values.

def add_one_function(x):
    x = x + 1
    return x

# This of course is the most basic way to use this function. We use the input argument of 3, assign
# the return value to a variable and print that variable, which will be 4.
return_value = add_one_function(1)
print(return_value)
# 2

# Notice we did not write add_one_function() below; note the parenthesis at the end. This means
# we are not calling the function we just defined, we are assigning a reference to it to the
# variable my_variable_is_a_function.
my_variable_is_a_function = add_one_function

# Now we can call the original function by using () on my_variable_is_a_function. This will
# call the function we hold the reference to with the argument of 1:
# my_variable_is_a_function(1)
print('Calling the original function through the reference in the new variable:')
print(my_variable_is_a_function(1))
# The original function performs its work and prints:
# 2

# What if we just print(my_variable_is_a_function) without the () on the end of
# my_variable_is_a_function?
print('The print() function applied to a function object shows us the address/id of the object:')
print(my_variable_is_a_function)
# This will print:
# <function add_one_function at 0x10219f0d0>
#
# Since we did not include (), the function was not called. The print() function works differently
# on different types of objects. When we print() a function object, that is the output you see,
# showing that my_variable_is_a_function is a function object. The hex number is the address or id
# of the function and will be different every time the program is run, which is true for all
# objects. However, the address or id will remain the same during the same program execution if
# the object has never been destroyed/garbage-collected.

# - - - - - - - - - -

# A common and useful real-world example of passing a function as an argument to another function
# is performing an operation called mapping, in which some operation (or function) is applied
# successively to all the items in a sequence, thus composing a new parallel sequence and the new
# (re-mapped) sequence is returned.
# For passing a function in this next exmaple we could pass my_variable_is_a_function or we could
# pass add_one_function because they point to the exact same object in memory. Let's prove this:
print('Both of these symbols point to exactly the same object/function:')
print(add_one_function)
print(my_variable_is_a_function)
# <function add_one_function at 0x1025b00d0>
# <function add_one_function at 0x1025b00d0>
#
# Notice that the identification of the object shows the original function name in both cases.
# This is because Python is also keeping track of the chain of references to the actual function
# object in memory and the print() function when used on function objects is designed to also
# show us the first or original symbol name assigned to the id or address. This can help us see
# if we are looking at the original reference to an object or a symbol which is further down
# a chain of references. But those details are just a little extra information at this point.
# At one level of Python, the identifiers of 'add_one_function' and 'my_variable_is_a_function'
# are just symbols, which can be variables, which can hold references to any kind of object. etc.

# Getting back to mapping by passing a function as an argument to another function.
# Lets re-map the sequence or list of [1, 2, 3, 4] by adding one to each item.
# So this is our imput which is a list object:
list_of_ints = [1, 2, 3, 4]

# A mapping function which can use any function as an argument to use during re-mapping the input.
# We refer to sequences, but in this case are only using lists. There are other python types we
# could use, such as iterators but that is a more advanced topic. Just know we are not limited to
# just using list objects in many such situations.
def mapper(repeated_function, sequential_input):
    output = []
    for item in sequential_input:
        # We passed a function in by reference and here we call it using ().
        new_item = repeated_function(item)  # This is one of the important parts
        output.append(new_item)  # By appending, we generate a sequence in a parallel order.
    return output

# So lets use our mapping function, and lets use it with our original add_one_function(), but
# when we pass in that argument, it is very important to leave off the () because we don't want to
# try to call it when we are passing it in to mapper(), we want to pass in the reference to the
# function object. Thus we will pass it in as just add_one_function. We could also just as well
# pass in my_variable_is_a_function because we know they point to the same function object.
# Our input is [1, 2, 3, 4] and we expect to get back [2, 3, 4, 5].

re_mapped_list = mapper(add_one_function, list_of_ints)

print('Passing a function argument to our mapper we get the output list:')
print(re_mapped_list)

print('And it works using the reference to our original function just as well:')
re_mapped_list_two = mapper(my_variable_is_a_function, list_of_ints)
print(re_mapped_list_two)


##
#

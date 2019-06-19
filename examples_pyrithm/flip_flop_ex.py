#! /usr/bin/env python3

####################################################################################################
# These are examples showing the usage of pyrithm.generator.flip_flop

import pyrithm


# Use the flip_flop_generator() to 'generate' an iterator capable of providing up to 6 flip flops:
limited_flip_flopper = pyrithm.generator.flip_flop.flip_flop_generator(6)

print("""
This example uses a generator function to 'generate' an iterator which will deliver 6 flip flops,
but we will attempt to iterate a total of 10 times. By design, iterators will raise a StopIteration
exception when they run out of iterations. Iterators can certainly be designed to provide an
infinite or unlimited number of iterations, but in this case we have generated an iterator with a
specific limit. If you know your iterator has a limit, then you almost certainly need a try-except
block to handle the expected StopIteration exception, which in this case we do have.""")

# TODO: Clean up the confusion here about types. This got a little messy.
# Basically should start over in this top part of the mini-tutorial and re-write it more clearly.
print("""
Let\'s look at some types. First, how print() displays the generator function,
which is imported as pyrithm.generator.flip_flop.flip_flop_generator:""")

print(pyrithm.generator.flip_flop.flip_flop_generator)
# <function flip_flop_generator at 0x10db29840>
print('And its type():')
# <class 'function'>
print(type(pyrithm.generator.flip_flop.flip_flop_generator))

print("""
So it is just a regular function. What makes it a generator, is the fact that it returns an
iterator object by using the yield keyword, instead of the typical return and of course it is also
structured as a generator. Now for the iterator object it returns or rather 'yields'. Let\'s first
look at how print() represents the iterator it and then at how the type() function
represents it:""")
print(limited_flip_flopper)
print(type(limited_flip_flopper))
print()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


for x in range(10):
    try:
        generated_iterator_thing = next(limited_flip_flopper)
    except StopIteration:
        print('You ran out of flip flops early.')
        print('You might need a flip flip generator which can provide more flip flops.')
        break  # Break out of the for loop. The current iterator is 'empty' and will error again.
    else:
        print(generated_iterator_thing)


print()
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print()

print("""
This example uses a generator to 'generate' an iterator which will is capable of delivering an
unlimited number of binary flip flops, although for a practicle example we will only ask the
iterator to generate 10. By design, iterators will raise a StopIteration exception when they run
out of iterations, but this one is desigend to iterate indefinitely when we 'generate' with a
specified max_flip_flops of 0. This generator also supports limits like the previous one.
""")

# Use the binary_flip_flop_generator() to 'generate' an iterator capable of providing unlimited
# binary flip flops:

unlimited_binary_flip_flopper = pyrithm.generator.flip_flop.binary_flip_flop_generator(0)

for x in range(10):
    generated_iterator_thing = next(unlimited_binary_flip_flopper)
    print(generated_iterator_thing)


print()
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print()

print("""
Next we show that the binary_flip_flop_generator() also supports finite iterator limits. In this
case we will generate the iterator with a specified limit of 2 binary flip flops (iterations.)
We will ask for 10 iterations, so we will hit the StopIteration exception which we will catch
gracefully.
""")

# Use the binary_flip_flop_generator() to 'generate' an iterator with a limit of 2
# iterations

limited_binary_flip_flopper = pyrithm.generator.flip_flop.binary_flip_flop_generator(2)

# We ask for 10 iterations which we know will exceed the limits of the generated iterator.
for x in range(10):
    try:
        generated_iterator_thing = next(limited_binary_flip_flopper)
    except StopIteration:
        print('You ran out of flip flops early.')
        print('You might need a flip flip generator which can provide more flip flops.')
        break  # Break out of the for loop. The current iterator is 'empty' and will error again.
    else:
        print(generated_iterator_thing)


##
#

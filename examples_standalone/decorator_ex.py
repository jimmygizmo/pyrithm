#! /usr/bin/env/python3
####################################################################################################

# A colorful illustration of decorators.
# This is an example showing a core Python feature and does not use any Pyrithm modules.

import colorama

# Cyan decorator
def cyan(any_function):
    # This is a decorator function, so it takes a function as an argument.
    # This and the other decorators here are designed to colorize our log function.
    # The @cyan annotation before any function passes it here for 'decoration', which can modify it
    # its behavior in certain ways.
    # It is important to note that 'any_function' is both a function AND an object and it is here
    # in the local scope, so we can return it too. We return it back with its original arguments
    # fully intact. Before we return it though, we give it a new ability such that the first thing
    # it does now, is use colorama to print the ANSI terminal control characters to set the
    # foreground color. But we don't
    def inner(*args, **kwargs):
        print(colorama.Fore.CYAN, end='')
        return any_function(*args, **kwargs)
    return inner

# Yellow decorator
def yellow(any_function):
    def inner(*args, **kwargs):
        print(colorama.Fore.YELLOW, end='')
        return any_function(*args, **kwargs)
    return inner

# Green decorator
def green(any_function):
    def inner(*args, **kwargs):
        print(colorama.Fore.GREEN, end='')
        return any_function(*args, **kwargs)
    return inner


# Change the decorator here to make log() output with different colors.
# Try @cyan, @yellow or @green
@cyan
def log(msg):
    print(msg)


log('A Decorator was used to add terminal color to the log function.')

# This example is not meant to be practical, since we only colorize log once and in a real
# application we would probably want to change log() colors to different colors depending
# on what we were logging. The point here is just to show how decorators work.


##
#

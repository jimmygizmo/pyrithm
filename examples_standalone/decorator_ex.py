#! /usr/bin/env/python3

# A colorful illustration of decorators and tutorial on their basic
# functionality.
#
# This is an example showing a core Python feature and does not use any Pyrithm
# modules. Everything is self-contained in this file. All information is
# contained in the code comments, the input and output examples and in the
# self-documenting function and symbol names.

# A decorator is a function that takes another function as the primary argument
# and extends, modifies or enhances the behavior of the original function
# without modifying the source code of the original function.

# A decorator and the @decorator_function_name syntax provide a simple syntax
# for calling higher order functions.

import colorama  # ANSI terminal color codes for colorizing console output
import functools  # When using decorators, functools.wraps improves things.
# See the end of this file for functools.wraps details and examples.


# White ANSI color decorator
def white(any_function):
    """Decorate function by first printing ANSI terminal white codes."""
    # This is a decorator function, so it takes a function as an argument.
    # This and the other decorators here are designed to colorize our log
    # function. The @white annotation before any function passes it here for
    # 'decoration', which can modify its behavior in certain ways. (Ignore the
    # fact that white is usually the default color.) It is important to note
    # that 'any_function' is both a function AND an object and it is here in
    # the local scope, so we can return it too. We return it back with its
    # original arguments fully intact. Before we return it though, we give it
    # a new ability such that the first thing it does now, is use colorama to
    # print the ANSI terminal control characters to set the foreground color.
    def wrapper(*args, **kwargs):
        print(colorama.Fore.WHITE, end='')
        return any_function(*args, **kwargs)
    return wrapper

# Yellow ANSI color decorator
def yellow(any_function):
    """Decorate function by first printing ANSI terminal yellow codes."""
    def wrapper(*args, **kwargs):
        print(colorama.Fore.YELLOW, end='')
        return any_function(*args, **kwargs)
    return wrapper

# Green ANSI color decorator
def green(any_function):
    """Decorate function by first printing ANSI terminal green codes."""
    def wrapper(*args, **kwargs):
        print(colorama.Fore.GREEN, end='')
        return any_function(*args, **kwargs)
    return wrapper

# Red ANSI color decorator
def red(any_function):
    """Decorate function by first printing ANSI terminal red codes."""
    def wrapper(*args, **kwargs):
        print(colorama.Fore.RED, end='')
        return any_function(*args, **kwargs)
    return wrapper

# Magenta ANSI color decorator
def magenta(any_function):
    """Decorate function by first printing ANSI terminal magenta codes."""
    def wrapper(*args, **kwargs):
        print(colorama.Fore.MAGENTA, end='')
        return any_function(*args, **kwargs)
    return wrapper


# Below we define different log functions as a simple way to log at different
# levels or in different situations. We can use the above decorators as a very
# simple and clean way to change the colorization of these log functions. In
# the real world you would probably use decorators for more complex situations,
# especially when it was not practical or desireable to modify the original
# functions themselves. Obviously in this example, we could just add a
# different colorizing line of code to each logging function, but the purpose
# here is to show how decorators are implemented and used with a simple and
# easy to understand example.

# Change the decorators below here to make the log_level() functions output
# with different colors.


@white
def log_info(msg):
    """Log INFO level message."""
    print(msg)

@yellow
def log_debug(msg):
    """Log DEBUG level message."""
    print(msg)

@green
def log_warn(msg):
    """Log WARN level message."""
    print(msg)

@red
def log_error(msg):
    """Log ERROR level message."""
    print(msg)

@magenta
def log_fatal(msg):
    """Log FATAL level message."""
    print(msg)


log_info('Logging at INFO level. The @white decorator is used.')
log_debug('Logging at DEBUG level. The @yellow decorator is used.')
log_warn('Logging at WARN level. The @green decorator is used.')
log_error('Logging at ERROR level. The @red decorator is used.')
log_fatal('Logging at FATAL level. The @magenta decorator is used.')

# - - - - - - - - - -

print()
log_info('Let\'s log at INFO, using @white so the following print() output '
         'is not magenta.')
log_info('Once you have sent an ANSI color code to the terminal, the terminal '
         'stays at that color.')
print()
log_info('Now for our bonus section about the __name__ and __doc__ properties '
         'of decorated functions.')
print()

# BONUS - __name__ and __doc__, the name and the docstring of decorated
# functions. How to fix problems with __name__ and __doc__ when using
# decorators.

# Let's look at the __name__ and the __doc__ properties of a decorated
# function. Looking at log_info()
print('Name (__name__) of the @white decorated log_info() function:')
print(log_info.__name__)
# wrapper
print('Docstring (__doc__) of the @white decorated log_info() function:')
print(log_info.__doc__)
# None

print()
print('Both of those are wrong!! Let\'s fix this situation using the '
      'functools.wraps module.')
print()

# This is a problem in many situations!
# It looks like using a decorator breaks the ability to use __name__ and
# __doc__ which are sometimes important things to be able to do, especially
# when trying to figure out how code is working under mysterious or complex
# circumstances or with large applications or APIs. Actually there are many
# important reasons you want these internal properties to be correct. There is
# a soluton and it is a special decorator provided by the functools module:
# @functools.wraps

# The below @cyan decorator is a little bit different than the others.
# Notice the use of the special @functools.wraps decorator applied to the
# inner wrapper() function.
# The actual usage looks like:
# @functools.wraps(decorated_function_argument)
# This goes immediately before the inner wrapper() function of the decorator.


# Cyan ANSI color decorator
def cyan(any_function):
    """Decorate function by first printing ANSI terminal cyan codes."""
    # The @functools.wraps decorator will fix __name__ and __doc__ for
    # decorated functions.
    @functools.wraps(any_function)
    def wrapper(*args, **kwargs):
        print(colorama.Fore.CYAN, end='')
        return any_function(*args, **kwargs)
    return wrapper

# And another logging function to decorate with @cyan
@cyan
def log_trace(msg):
    """Log TRACE level message."""
    print(msg)

log_trace('Logging at TRACE level. The @cyan decorator is used.')
print()

# Let's look at the __name__ and the __doc__ properties of the decorated
# function, when @functools.wraps(decorated_function_argument) is used in the
# involved decorator:
# Looking at log_trace()
print('Name (__name__) of the @cyan decorated log_trace() function:')
print(log_trace.__name__)
# log_trace
print('Docstring (__doc__) of the @cyan decorated log_trace() function:')
print(log_trace.__doc__)
# Log TRACE level message

# Name (__name__) of the @cyan decorated log_trace() function:
# log_trace
# Docstring (__doc__) of the @cyan decorated log_trace() function:
# Log TRACE level message.

# Works like magic! Now your decorated functions can be introspected and
# __name__ and __doc__ will work correctly.


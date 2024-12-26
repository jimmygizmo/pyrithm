#! /usr/bin/env python

import time


# I've seen both of these forms used for module version.
# TensorFlow for example has tf.__version__ but I see here that the time module does not.
# My conclusion is that this varies between modules but I'll update as I research this further
# since I have not looked at the docs yet. This script, as with those scripts in the /nuggets/ dir in general,
# is here to test a few things regarding this question and document the results, prior to a more formal
# example or illustrative script. Sometimes When I nail down important but small concepts, I will just incorporate
# those into other Pyrithm example scripts and modules, whatever makes the most sense.
print()

print("time.__version__  ERROR - no such attribute")
# UNCOMMENT NEXT LINE TO DEMONSTRATE:
# print(time.__version__)  # ERROR: AttributeError: module 'time' has no attribute '__version__'
print()

print("time.version.VERSION  ERROR - no such attribute")
# UNCOMMENT NEXT LINE TO DEMONSTRATE:
# print(time.version.VERSION)  # ERROR: AttributeError: module 'time' has no attribute 'version.VERSION'
print()


# UPDATE: So both of those seem to be specific to Tensorflow (the main module.)

# UPDATE 2: Apparently none of standard library modules has __version__ and just follow their Python's version.

# UPDATE 3: Info indicates it is recommended but optional for module authors to use __version__

# UPDATE 4: .version and .version.VERSION and similar facilities might be a tradition among the larger
#           and more complex libraries/packages like Numpy, TensorFlow, Pandas, etc.



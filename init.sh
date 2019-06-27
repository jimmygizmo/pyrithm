#! /usr/bin/env bash
###############################################################################
# This script will create your Python virtual environment in a best-practice
# configuration which also maximises compatibility with the VSCode IDE. VSCode
# is currently the IDE preferred by most Python developers. VSCode will
# automatically detect and activate a virtual environment named .venv and will
# look for some modules which we will install from this init script in order to
# provide you with important functionality such as static code analysis.

# IMPORTANT: Your Python 3 interpreter is expected to be available as
# 'python3'.
# - For developers on MacOS:
# Homebrew is by far the best way to install Python on your Mac and is also
# even more preferred when you want to run both Python 2 and Python 3 on the
# same system. When Homebrew is used, Python 3 will be available as 'python3'
# and Python 2 will be available as 'python'.
# - For developers on Windows: (Windows Python development recommendations are
# forthcoming.)

# Create the python virtual environment.
python3 -m venv .venv

# Activate the new python virtual environment.
source .venv/bin/activate

# Upgrade the virtual environment's setuptools and pip.
# New virtual environments created with the 'venv' module frequently come with
# a setuptools and pip that are many versions back. In most cases it is a good
# idea to upgrade these tools to the latest versions.
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools

# Install packages to support and enhance IDE operation, particularly VSCode.
python3 -m pip install pylint  # Static code analysis for Python
python3 -m pip install autopep8  # Automatic PEP8 code reformatting
python3 -m pip install rope  # Python code refactoring library

# Install project-specific python depdendencies
python3 -m pip install -r requirements.txt

# Install this project's package
# For development, we will install this project's package using the -e option
# so that pip will install it into the venv using symlinks. In this way we can
# make changes to the module which will be picked up upon each new execution
# using the module.
python3 -m pip install -e .


###############################################################################
# Before you first run this project's Python code in any shell you will always
# need to activate the Python virtual environment unless you plan to install
# all requirements globally or unless your IDE provides some other library
# loading/access mechanism and that is how you are running code. Most IDEs,
# when running this program for you, usually in a new, visible terminal window,
# will do the same thing as this command:
#### source .venv/bin/activate
#
# For development in an IDE, you may need to configure the IDE to recognize and
# automatically activate the new python virtual environment, however many
# popular IDEs such as VSCode can automatically see and activate this
# environment in the .venv directory in which we create it, at the base of the
# project directory or repository.
###############################################################################

# Modules installed to support pylint (versions may differ slightly):
# astroid==2.2.5
# isort==4.3.20
# lazy-object-proxy==1.4.1
# mccabe==0.6.1
# pylint==2.3.1
# six==1.12.0
# typed-ast==1.4.0
# wrapt==1.11.1

# Modules installed to support autopep8 (versions may differ slightly):
# autopep8==1.4.4
# pycodestyle==2.5.0

# Modules installed to support rope
# rope==0.14.0



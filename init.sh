#! /usr/bin/env bash

# TODO: As noted in other such files recently, a NEW VERSION OF THIS IS NEEDED.
# I now use Pyenv and Pyenv Virtualenv exclusively so the virtual environment
# aspect as changed. The lower part of this init.sh file will likely not change
# much.

# TODO: Update. Below here, instructions RE virtual env are now deprecated.
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

# TODO: NOTE: Below here the instructions should be mostly or totally valid.
# A re-write of this file is pending. I need to write a master Pyenv instruction
# doc to include in all of my Python projects.
# NOTE: Under Pyenv/Pyenv-Virtualenv, you can use the python3 command as below
# but it is fine and probably preferable to just use 'python'. The usage of
# 'python3' was more relevant a few years ago when there was a lot more Python 2
# still in use and also it was more relevant when I was mostly using Homebrew-
# installed Python. Using Pyenv is much better, even required .. so you can
# properly match all versions and properly manage Python and libraries
# for many projects.
###############################################################################



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

# Install project-specific python dependencies
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

# TODO: Check and update. This is the recent output of pip freeze now under a much higher Python
# version (3.10.4). About 3 years have past so the amount of change will be interesting to see:
# I see some new modules (dependencies 2nd or nth gen.): dill, platformdirs, toml, tomli, tomlkit.
# Some modules are gone now: six, typed-ast.
# Six is probably gone now because a lot of Python 2 to Python 3 migration work has been completed.
# All versions have gone up as expected.
# Wow, I did not expect to see this git format for the Pyrithm local "editable" install. I expected
# only that the install was done using a symlink so I will need to learn more about the git reference.
# ** The -e option is so that pip does not copy but rather links the files so you can work on them live
# and test them live, so that is more for developers of Pyrithm (myself) and users could probably leave off
# the -e but I honestly don't know exactly how the -e option and the '.' path interact with pip install
# with respect to this surprising git URL in the pip freeze. I know you can in stall from git URLs but in this
# this case I did not expect that from my "pip install -e ." step to install Pyrithm itself (from the current
# dir.
# I'm not going to continue tracking which 2nd and nth gen dependencies came from what 1st gen as I was
# doing before. I will just list the pip freeze output, unless there is something really important to note.
# Version pinning strategies are another matter with some overlapping concerns.

#(ve.pyrithm) ➜  pyrithm git:(master) ✗ date
#Thu Jun 16 19:35:43 PDT 2022
#(ve.pyrithm) ➜  pyrithm git:(master) pip freeze
#astroid==2.11.6
#autopep8==1.6.0
#dill==0.3.5.1
#isort==5.10.1
#lazy-object-proxy==1.7.1
#mccabe==0.7.0
#platformdirs==2.5.2
#pycodestyle==2.8.0
#pylint==2.14.2
#-e git+ssh://git@github.com/jimmygizmo/pyrithm.git@5d090504b53d762b26c3d197731fdbee48cea03f#egg=Pyrithm
#rope==1.1.1
#toml==0.10.2
#tomli==2.0.1
#tomlkit==0.11.0
#wrapt==1.14.1


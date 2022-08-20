#! /usr/bin/env bash


################################################################################

# PYENV INSTALLATION OF PYTHON AND CREATION OF VIRTUAL ENVIRONMENT

# These instructions assume you are using Pyenv and Pyenv-Virtualenv to
# manage your Python installations and Python virtual environments for your
# projects. If you are not using Pyenv, you should strongly consider it.
# There really is no other way for a professional developer to maintain
# project-specific Python versions and project-specific virtual environments
# and their isolated module libraries and to do it correctly and efficiently,
# without using Pyenv. It works simply and very well on all platforms.
# https://github.com/pyenv/pyenv

# Python version currently used for development, testing and deployment:
# Python 3.10.4

# A .python-version file at the root of project is used to select the
# Pyenv virtual environment to activate.
# YOU WILL NEED TO CREATE THE PYENV VIRTUAL ENVIRONMENT MANUALLY BEFORE HAND.
# Do this before anything else.

# If necessary, have Pyenv install the required/preferred version of Python.
# pyenv install 3.10.4
#
# * In practice, many versions of Python and libraries will likely work fine,
# but some testing and deployment procedures might require exact version
# matching. In fact, when you use Pyenv, it is easy to always match all
# versions of everything exactly and this is how you should work;
# in a precise manner. In the long run, the benefits pay off a great deal.

# Now create the virtual environment with the required name:
# pyenv virtualenv 3.10.4 ve.pyrithm

# Once this is done, the ve.pyrithm virtual environment will be active
# in any directory or sub-directory anywhere within the project, all thanks
# to the .python-version file at the root of the project directory. This
# file contains a single line with the name of the virtual environment:
# 've.pyrithm'.


################################################################################

# UPGRADE PYTHON INSTALLATION TOOLS IN THE NEW PROJECT VIRTUAL ENVIRONMENT

# The below pip install commands must be done within the project so that the
# ve.pyrithm virtual environment is active and thus the installations will be
# done there. This runs the pip binary which belongs to the active project
# virtual environment and knows to operate within the virtual environment.
# Your system Python is not involved and will not be touched and this is one of
# the multiple reasons to use a virtual environment and for this you should be
# using Pyenv, because it is far superior to any other method.


# Upgrade the virtual environment's pip, wheel and setuptools.
# New virtual environments usually come with installation utilities that are
# a few versions back. In most cases, it is a good idea to upgrade these tools
# to the latest versions.
pip install --upgrade pip

pip install --upgrade setuptools

# TODO: We're getting into wheel installs and pre-building/storing the
#       archives needed to build a container for a python app. Eliminate remote
#       repos.
#       (Not necessarily for Pyrithm, but this is the init.sh file I will be
#       using for all Python projects, including many that run in containers
#       and for which you want stable images with changes under control.)
pip install --upgrade wheel


# INSTALL MODULES WHICH ENHANCE PYTHON SOFTWARE DEVELOPMENT AND TESTING

# Python Software Development Tools - Source Code Analysis and Reformatting

# Installing these libraries will activate features in some IDEs and are
# required to use those features in the IDE. This was the case for VSCode,
# as of 2019.
# TODO: Confirm and update the situation for both VSCode and ItelliJ IDEs
#       to clarify which modules activate or are required for which features
#       in each IDE. Now in 2022, some of this has no doubt changed and
#       needs to be updated.


pip install pylint  # Static code analysis for Python
pip install autopep8  # Automatic PEP8 code reformatting
pip install rope  # Python code refactoring library

# Install project-specific python dependencies
pip install -r pinned-requirements.txt

# Install this project's package
# For development, we will install this project's package using the -e option
# so that pip will install it into the venv using symlinks. In this way we can
# make changes to the module which will be picked up upon each new execution
# using the module.
pip install -e .


################################################################################

# For development in an IDE, you may need to configure the IDE to recognize and
# automatically activate the new python virtual environment, but recent IDEs
# often need only a little help or no help at all and detect it automatically.
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


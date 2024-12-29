#! /usr/bin/env bash

################################################################################

# PYENV INSTALLATION OF PYTHON AND CREATION OF VIRTUAL ENVIRONMENT

# These instructions assume you are using Pyenv and Pyenv-Virtualenv to
# manage your Python installations and Python virtual environments for your
# projects. If you are not using Pyenv, you should strongly consider it.
# There really is no other way for a professional developer to maintain
# project-specific Python versions and project-specific virtual environments
# and their isolated module libraries and to do it correctly and efficiently,
# without using Pyenv. I recommend avoiding ALL other tools like this. Use
# Pyenv as it is the only clean solution which is in sync with the Python
# ecosystem. Pyenv works in a simple way and very well on all platforms.
# https://github.com/pyenv/pyenv

# Python version currently used for development, testing and deployment:
# Python 3.10.4  TODO: Now up to 3.12.4 but much of the project needs testing. TODO: ADD UNIT TESTS EVERYWHERE

# A .python-version file at the root of project is used to select the
# Pyenv virtual environment to activate.
# YOU WILL NEED TO CREATE THE PYENV VIRTUAL ENVIRONMENT MANUALLY BEFORE HAND.
# Do this before anything else.

# If necessary, have Pyenv install the required/preferred version of Python.
# pyenv install 3.10.4     TODO: Now up to 3.12.4
#
# * In practice, many versions of Python and libraries will likely work fine,
# but some testing and deployment procedures might require exact version
# matching. In fact, when you use Pyenv, it is easy to always match all
# versions of everything exactly and this is how you should work;
# in a precise manner. In the long run, the benefits pay off a great deal.

# Now create the virtual environment with the required name:
# pyenv virtualenv 3.10.4 ve.pyrithm     TODO: Now up to 3.12.4

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
# This should take pip from version 22.0.4 to 22.2.2
# TODO: Update docs for 3.12.4 after testing full project:
#          This should take pip from version 24.0 to 24.3.1

pip install --upgrade setuptools
# This should take setuptools from version 58.1.0 to 65.1.0
# TODO: For 3.12.4: This should take setuptools to 75.6.0

# TODO: We're getting into wheel installs and pre-building/storing the
#       archives needed to build a container for a python app. Eliminate remote
#       repos.
#       (Not necessarily for Pyrithm, but this is the init-project.sh file I
#       will be using for all Python projects, including many that run in
#       containers and for which you want stable images with changes under
#       source control.)
pip install --upgrade wheel
# This should install wheel 0.37.1
# TODO: For 3.12.4: This should take wheel to 0.45.1


# INSTALL MODULES WHICH ENHANCE PYTHON SOFTWARE DEVELOPMENT AND TESTING

# Python Software Development Tools - Source Code Analysis and Reformatting

# Installing these libraries will activate features in some IDEs and are
# required to use those features in the IDE. This was the case for VSCode,
# as of 2019.
# TODO: Confirm and update the situation for both VSCode and ItelliJ IDEs
#       to clarify which modules activate or are required for which features
#       in each IDE. Now in 2022, some of this has no doubt changed and
#       needs to be updated.


# TODO: MOST of these versions will likely have changed now that we are on Python 3.12.4

# TODO: There are a lot of other good Python linters available now as we enter 2025. Check out this article:
# https://inventwithpython.com/blog/2022/11/19/python-linter-comparison-2022-pylint-vs-pyflakes-vs-flake8-vs-autopep8-vs-bandit-vs-prospector-vs-pylama-vs-pyroma-vs-black-vs-mypy-vs-radon-vs-mccabe/
# TODO: All of the below needs to be updated in light of this. We might come up with a whole new set of linters to use now.
# But I have not critical need for additional linting, but its always good to look at new stuff like this. PyCharm does fine with linting,
# and I use MyPy a lot also. In the recent past, PyCharm used to seem to detect some of these other linters I install
# here in this older setup script, but I don't know all the details about PyCharm's linting now in 2025. I'll bring this up to date shortly.


pip install pylint  # Static code analysis for Python
# This brings in the following:
# astroid==2.11.7
# dill==0.3.5.1
# isort==5.10.1
# lazy-object-proxy==1.7.1
# mccabe==0.7.0
# platformdirs==2.5.2
# pylint==2.14.5
# tomli==2.0.1
# tomlkit==0.11.4
# wrapt==1.14.1


pip install autopep8  # Automatic PEP8 code reformatting
# This brings in the following:
# autopep8==1.7.0
# pycodestyle==2.9.1
# toml==0.10.2


pip install rope  # Python code refactoring library
# This brings in the following:
# packaging-21.3
# pyparsing-3.0.9
# pytoolconfig-1.2.2
# rope-1.3.0


# With only the above modules and their dependencies installed to assist
# Python development, pip freeze will show:
# astroid==2.11.7
# autopep8==1.7.0
# dill==0.3.5.1
# isort==5.10.1
# lazy-object-proxy==1.7.1
# mccabe==0.7.0
# packaging==21.3
# platformdirs==2.5.2
# pycodestyle==2.9.1
# pylint==2.14.5
# pyparsing==3.0.9
# pytoolconfig==1.2.2
# rope==1.3.0
# toml==0.10.2
# tomli==2.0.1
# tomlkit==0.11.4
# wrapt==1.14.1


# Install project-specific python dependencies
pip install -r pinned-requirements.txt


# Install this project's package
# For development, we will install this project's package using the -e option
# so that pip will install it into the venv using symlinks. In this way we can
# make changes to the module which will be picked up upon each new execution
# using the module.
pip install -e .
# TODO: Things seem to be working fine without doing this, but maybe the IDE is helping. Looking into this later.

################################################################################

# For development in an IDE, you may need to configure the IDE to recognize and
# automatically activate the new python virtual environment, but recent IDEs
# often need only a little help or no help at all and detect it automatically.

###############################################################################

# IMPORTANT - Regarding how the installation of Pyrithm itself seems linked to
# a specific git revision based on pip freeze output:
#-e git+ssh://git@github.com/jimmygizmo/pyrithm.git@5d090504b53d762b26c3d197731fdbee48cea03f#egg=Pyrithm

# Wow, I did not expect to see this git format for the Pyrithm local "editable" install. I expected
# only that the install was done using a symlink so I will need to learn more about the git reference.
# ** The -e option is so that pip does not copy but rather links the files so you can work on them live
# and test them live, so that is more for developers of Pyrithm (myself) and users could probably leave off
# the -e but I honestly don't know exactly how the -e option and the '.' path interact with pip install
# with respect to this surprising git URL in the pip freeze. I know you can install from git URLs but in this
# this case I did not expect that from my "pip install -e ." step to install Pyrithm itself (from the current
# dir.)

# This is our current pip freeze output, not that all project init steps are complete:
# astroid==2.11.7
# autopep8==1.7.0
# colorama==0.4.5
# dill==0.3.5.1
# isort==5.10.1
# lazy-object-proxy==1.7.1
# mccabe==0.7.0
# packaging==21.3
# platformdirs==2.5.2
# pycodestyle==2.9.1
# pylint==2.14.5
# pyparsing==3.0.9
# -e git+ssh://git@github.com/jimmygizmo/pyrithm.git@a04d85ba25d01658245c34e89b8ea02bca0be88c#egg=Pyrithm
# pytoolconfig==1.2.2
# rope==1.3.0
# toml==0.10.2
# tomli==2.0.1
# tomlkit==0.11.4
# wrapt==1.14.1


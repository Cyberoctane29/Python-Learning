# Create a virtual environment
python -m venv dir_name

#makes a copy of the python in the computer

# for activation  of that environment-
dir_name\Scripts\activate
#or
.\myenv\Scripts\Activate.ps1

# The command dir_name\Scripts\activate working suggests that the activation script is being correctly executed even though the typical method
# in PowerShell is to use the Activate.ps1 script. This can happen because of a few reasons:
#
# Automatic Resolution: PowerShell might be resolving the activate script to the correct executable script (e.g., activate.bat or Activate.ps1)
# in the Scripts directory.
#
# File Association: The activate script without an extension might be correctly associated with a script interpreter that PowerShell can execute
# directly.
#
# Let's break it down:
#
# PowerShell Specifics
# PowerShell can execute .ps1 files, and sometimes it can also run scripts that don('t have an extension if they are in the current directory '
# or in a directory that is part of the PATH environment variable. When you ran dir_name\Scripts\activate, PowerShell might have automatically
# resolved it to Activate.ps1 because it is in the same directory.)

import pandas
#ok after all of this if we check my trying to importing pandas it show there is no such module as we have a completely different environment
# of python now
#so here we can import python

pip3 install pandas
python
import pandas as pd
pd.__version__
output:
'2.2.2'

#if we wanted a particular version of python
pip3 install pandas==1.4.4

#to deactivate the virtual env-to come out of the folder in which the python is installed then
deactivate

#what if we wanted to give someone the project we are working on for them to work upon it they would require the package installed info in that
# particular python environment, for this to happen run this in the env folder's terminal

pip freeze
#to add into a text file
pip freeze>requirement.txt

#now we send this txt file to the person who wants the info
#they will run

pip install -r requirements.txt

#those packages will installed in their computer


#to check which shell is being used
# For Command Prompt (cmd.exe):
# Run the following command:
#
# cmd
# Copy code
# echo %COMSPEC%
# Output Interpretation:
#
# If you are in the Command Prompt, the output will typically be:
# plaintext
# Copy code
# C:\Windows\System32\cmd.exe
# For PowerShell:
# Run the following command:
#
# powershell
# Copy code
# $PSVersionTable.PSVersion
# Output Interpretation:
#
# If you are in PowerShell, the output will be a table showing the version of PowerShell, similar to:
# plaintext
# Copy code
# Major  Minor  Build  Revision
# -----  -----  -----  --------
# 5      1      19041  1237
# This output confirms you are using PowerShell.
# For Git Bash or WSL:
# Run the following command:
#
# bash
# Copy code
# echo $SHELL
# Output Interpretation:
#
# If you are in Git Bash, the output will typically be:
# plaintext
# Copy code
# /bin/bash
# If you are in WSL (Windows Subsystem for Linux), the output will be similar, usually:
# plaintext
# Copy code
# /bin/bash

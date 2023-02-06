# Scripting

# Shorter pieces of code that allow us to do things we would otherwise have to do manually
# Unlike programs, scripts are one file and do not need to be compiled
# API's tend to use script

# Scripts use less or no abstractions and are not as flexable as programs. But they are much easier to read and write.

# Scripts are almost always written in 'high level' language( easy to read) - Python, Bash, Ruby, Node.js

# Why Python

# Open Source
# Many libraries
# Easy to understand
# Large community
# Language interoperability (can talk to other languages, OS's and software)

# Why is Scripting important for DevOps engineers?

# Automation -. of mundane tasks


# 7 core modules in Python
# Sys
# OS
# Subprocesses
# Math
# Random
# DateTime
# JSON

# Sys module scripts
import json
import os
import sys

print(sys.version)

# OS module script

print(os.getcwd()) # get currently working directory

# os.chdir("C:\Users\ashar\PycharmProjects\pythonProject\tech201_python_scripting") # Changes directory

# os.mkdir("path") # Makes new directory

# Subprocess module script
# Can be used to create and interact with subprocesses being managed by our Python interpreter
import subprocess

subprocess.run(["python", "Hello_World!.py"])

# Math module scripts
import math

pi = math.pi
pi_string = str(pi)
print(f"The value of pi id {pi}")

# Random module scripts
import random

randnum = random.randrange(1, 10)
print(randnum)

# DateTime module scripts
import datetime

whatisthedate = datetime.datetime.now()
print(whatisthedate)

# JSON module script

import json

x = {
    "name": "John",
    "age": "30",
    "city": "London"
}

y = json.dumps(x)

print(y)








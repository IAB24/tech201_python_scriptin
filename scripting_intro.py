#Scripting

# Short pieces of code that allow us to do things we would otherwise do manually.
# Unlike programs, scripts are one file and not need to be compiled.
# API's tend to use scripts

# Scripts use less or no abstraction and are not as flexible as programs but are much easier to read and write.

# Scripts are almost always written in 'high level' language (easy to read) - Python, Bash, Ruby. Node.js

#Why Python

# Open Source
# Many libraries
# Large community
# Easy to understand
# Language interoperability (can talk to other languages, OS's and software)

# Why is Scripting important for DevOps engineers?

# Automation -> of mundane tasks
# Take a backup, fetch IP addresses, automate CRUD etc

# 7 core modules in Python

# Sys
# Os
# Subprocesses
# Math
# DateTime
# JSON
# Random

# Sys module script
import sys

print(sys.version)

# os module script
import os
print(os.getcwd()) # get current working directory

# os.chdir() #change directory

# os.mkdir("path") # makes new directory

# Subprocess module script

# Can be used to create and interact with subprocesses being managed by our pythoin interpreter.
import subprocess

subprocess.run(["python", "hello_world.py"])

# Math module scripts
import math

pi = math.pi
pi_string = str(pi)

print("The value of pi is " + pi_string)

# Random module scripts
import random
randum = random.randrange(1, 10)
print(randum)

# DateTime module scripts
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate)

# JSON module script
import json
x = {
    "name": "John",
    "age": 30,
    "city": "London"

}

y = json.dumps(x)
print(y)





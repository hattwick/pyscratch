#! Python3 routine for calling system information
# Influenced by Coursera Python for Everybody and various references

import os
from subprocess import call

# Retrieve environmentals
print(os.getuid())
print(os.getgid())
print(os.getlogin())
print(os.getcwd())
print(os.getenv("PATH"))


# Interactive commands
os.system('ls -lrt')

command  = input("Press Enter to run ls -lrt")
call(["ls", "-lrt"])
<<<<<<< HEAD
# -30- 
=======

# -30- 
>>>>>>> origin/master

#! Python3 routine for calling system information
# Influenced by Coursera Python for Everybody and various references
# comment

import os
from subprocess import call

# Retrieve environmentals
print(os.getuid())
print(os.getgid())
print(os.getlogin())
print(os.getcwd())
print(os.getenv("PATH"))

# -30- 
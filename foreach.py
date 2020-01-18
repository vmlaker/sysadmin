""" Execute a command for each word in a file.
"""

import sys
from subprocess import call

input_file = sys.argv[1]
command_template = sys.argv[2]

with open(input_file) as ff:
    items = (x.strip() for x in ff.readlines())

for item in items:
    command = command_template.format(item)
    print(command)
    call(command, shell=True)

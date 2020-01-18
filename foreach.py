""" Execute a command for each line in stdin.
"""

import sys
from subprocess import call

command_template = sys.argv[1]

for item in (x.strip() for x in sys.stdin):
    command = command_template.format(item)
    print(command)
    call(command, shell=True)

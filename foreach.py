""" Execute a command for each line in stdin.

For example, to run "wc" serially on every file:
    ls | python foreach.py 'wc -l {}'
Or, to run in parallel:
    ls | python foreach.py '!' 'wc -l {}'
"""

import sys
from subprocess import call

command_template = sys.argv[1]
parallel = command_template == '!'

if not parallel:
    for item in (x.strip() for x in sys.stdin):
        command = command_template.replace('{}', item)
        print(command)
        call(command, shell=True)
    sys.exit(0)

# If running concurrently:
command_template = sys.argv[2]
from concurrent.futures import ProcessPoolExecutor as Executor
executor = Executor()
for item in (x.strip() for x in sys.stdin):
    command = command_template.replace('{}', item)
    print(command)
    executor.submit(call, command, shell=True)
executor.shutdown()
sys.exit(0)

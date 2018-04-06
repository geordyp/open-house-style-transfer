import subprocess
from shlex import split
from collections import namedtuple
from functools import reduce
import datetime;


proc_output = namedtuple('proc_output', 'stdout stderr')


def makeCopys():
    t = datetime.datetime.now().timestamp()
    with open('../inputs-outputs/in-%s.jpg' % t, 'wb') as f:
        f.writelines(open('static/styletransfer/images/input.jpg', 'rb').readlines())

    with open('../inputs-outputs/out-%s.jpg' % t, 'wb') as f:
        f.writelines(open('static/styletransfer/images/output.jpg', 'rb').readlines())


def pipeline(starter_command, *commands):
    if not commands:
        try:
            starter_command, *commands = starter_command.split('|')
        except AttributeError:
            pass
    starter_command = _parse(starter_command)
    starter = subprocess.Popen(starter_command, stdout=subprocess.PIPE)
    last_proc = reduce(_createPipe, map(_parse, commands), starter)
    return proc_output(*last_proc.communicate())


def _createPipe(previous, command):
    proc = subprocess.Popen(command, stdin=previous.stdout, stdout=subprocess.PIPE)
    previous.stdout.close()
    return proc


def _parse(cmd):
    try:
        return split(cmd)
    except Exception:
        return cmd

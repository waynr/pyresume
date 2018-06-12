# -*- coding: utf-8 -*-

import subprocess


def get_subprocess_output(command):
    """Call subprocess and return stdout normalized into Python string.
    """
    output = subprocess.check_output(command, shell=True)
    return output.rstrip().decode('UTF-8')

#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes a function safely."""
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as e:
        sys.stderr.write('Exception: {}\n'.format(e))
        return None

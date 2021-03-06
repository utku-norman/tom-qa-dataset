from argparse import ArgumentTypeError
import errno
import os


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr # input expression in which the error occurred
        msg  # explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


def is_file(f):
    try:
        open(f, 'r')  # return an open file handle
    except IOError:
        raise ArgumentTypeError("{0} does not exist".format(f))
    return f


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
    return path


def remove_extension(path):
    return os.path.splitext(os.path.basename(path))[0]

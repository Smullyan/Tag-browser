#! /usr/bin/python

import os


def _get_filepath(filename):
    # using os.path.exists rather than os.path.isfile because
    # os.path.exists checks directories also
    # requires use of quotes (" ") in filename to execute
    # the return value will then be used in a sorted data file.
    if os.path.exists(filename) is True:
        return os.path.abspath(filename)
    else:
        print "File does not exist."
        # I think this is correct
        return 0


"""
def _ask_for_comments:

def _store_tags:

def tag:
"""

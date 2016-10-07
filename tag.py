#!/usr/bin/python

import os
import re


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


def _ask_for_comment():
    comment = raw_input(">> ")
    return comment


def _get_tags(comment):
    # Store tags as a list
    tags = re.findall('(?<=#)\w+', comment)
    return tags

    # I'm thinking of storing filename, file path, comment and tags into an output file
    # Make code to be able to identify '#' symbol and mark word after that
    # Store the tag to output file above and maybe another output file to do metadata analysis
    # Then add all those functions to a single function.

"""
Maybe use Tuples to record data?
That said, Tuples can't be updated, so maybe that's a bad way to store data.

def _ask_for_comments:

def _store_tags:

def tag:
"""

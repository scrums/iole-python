#!/usr/bin/env/python


# This file is meant to start execution, and perform the necessary tasks only if the parameter is a csv file
import json
import sys
import tree_init


def main(argv):

    address = argv # set address to be the first parameter
    # should not execute if file address is not a valid one
    valid = False
    try:
        csv = open(address, 'r')
        valid = True
    except IOError:
        print("File does not exist; ")
        valid = False

    if not valid or not address.endswith(".csv"):
        print("Invalid file")
        exit(1)

    str_csv = ""

    for line in csv:
        str_csv += line

    # we need to send this back to the json
    pair_csv = tree_init.run(str_csv)


# Execution start

main(sys.argv[1])







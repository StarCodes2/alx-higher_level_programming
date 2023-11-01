#!/usr/bin/python3
"""Prints the name or strings passed to it."""


def say_my_name(first_name, last_name=""):
    """Prints the value of first_name anf last_name with additional strings"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))

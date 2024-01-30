#!/usr/bin/python3
"""
Module that defines a locked class.
"""


class LockedClass:
    """
    Prevent the user from instantiating LockClass attributes for anything but attributes called 'first name'.
    """

    __slots__ = ["first_name"]

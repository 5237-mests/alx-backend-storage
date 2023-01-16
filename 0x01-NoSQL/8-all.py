#!/usr/bin/env python3
"""Module for task 8
"""


def list_all(mongo_collection):
    """Return all doc inside give collection"""
    return [el for el in mongo_collection.find()]

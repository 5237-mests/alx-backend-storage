#!/usr/bin/env python3
"""Module for task 9
"""


def insert_school(mongo_collection, **kwargs):
    """Return id of inserted collection doc"""
    myid = mongo_collection.insert_one(kwargs)
    return myid.inserted_id

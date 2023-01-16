#!/usr/bin/env python3
"""Module for task 11
"""


def schools_by_topic(mongo_collection, topic):
    """Find all"""
    return mongo_collection.find({'topics': topic})

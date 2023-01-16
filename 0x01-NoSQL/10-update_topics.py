#!/usr/bin/env python3
"""Module for task 10
"""


def update_topics(mongo_collection, name, topics):
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

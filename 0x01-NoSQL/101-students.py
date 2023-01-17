#!/usr/bin/env python3
"""Module for task 101
"""


def top_students(mongo_collection):
    """Sorts list"""
    stud = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1}
            },
        ]
    )
    return stud

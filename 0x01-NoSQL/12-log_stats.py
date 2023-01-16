#!/usr/bin/env python3
"""Module for task 12
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    def log_stats(my_collection):
        """prints all stats"""
        print('{} logs:'.format(len(list(my_collection.find()))))

        for methodn in method:
            numl = list(my_collection.find({'method': methodn}))
            print('\tmethod {}: {}'.format(methodn, len(numl)))

        stat = list(my_collection.find({'method': 'GET', 'path': '/status'}))
        print('{} status check'.format(len(stat)))

    log_stats(nginx_collection)

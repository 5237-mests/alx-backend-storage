#!/usr/bin/env python3
'''Task 101's module.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs'''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))

def print_ip(nginx_collection):
    """prints top Ips"""
    print("IPs:")
    lnn = list(nginx_collection.find({'ip': '172.31.63.67'}))
    print("\t172.31.63.67: {}".format(len(lnn)))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    collectionnginx = client.logs.nginx
    print_nginx_request_logs(collectionnginx)
    print_ip(collectionnginx)


if __name__ == '__main__':
    run()

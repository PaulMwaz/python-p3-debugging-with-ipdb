#!/usr/bin/env python3

import ipdb

def plus_two(num):
    ipdb.set_trace()  
    num = num + 2
    return num


if __name__ == "__main__":
    print(plus_two(3))  

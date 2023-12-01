#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    # for i in range(len(sys.argv)-1):
    #     if (i > 0):
    #         print(f"{sys.argv[i]} ", end='')
    print(f"{len(sys.argv)-1} argument:")
    for i in range(len(sys.argv)-1):
        print(f"{i+1}: {sys.argv[i+1]}")
else:
    print("0 arguments.")
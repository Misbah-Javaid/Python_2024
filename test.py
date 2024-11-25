#! /usr/bin/env python
import sys

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greet

print(greet("world"))
print(greet("Misbah"))
print('Misbah')
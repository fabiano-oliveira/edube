import platform
import os
import sys

def print_head(title):
    print()
    print(title)
    print("-" * 30)

print_head("platform")
print(dir(platform), sep=", ")

print_head("os")
print(dir(os), sep=", ")

print_head("outros")
print(platform.platform())
print(platform.machine())
print(platform.processor())
print(platform.version())
for p in sys.path:
    print(p)
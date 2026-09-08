import os, sys
from hello_world_func import *

hello_world_func("Alice")

# List the contents of the WORKDIR
entries = os.listdir("/home/python_app/test_data/")
print(entries)
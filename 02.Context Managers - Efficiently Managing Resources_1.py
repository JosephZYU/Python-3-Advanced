# https://youtu.be/-aKFBoZpiqA
"""
# Basic ways to use context manager

f = open('sample.txt', 'w')

f.write('Random Text by Joseph Yu')

f.close()
"""


# with open('sample.txt', 'w') as f:
#     f.write('Random Text by Joseph Yu')

"""
class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


# 🧠 with Open_File() as f:
# Use the with methdo to streamline the process
with Open_File('sample.txt', 'w') as f:
    f.write('Testing')

print(f.closed)
"""

# Use the context lib module & import the context manager decotator


# 🎯🧐 Review on the tear down method: try and finally
# Ref - https://youtu.be/-aKFBoZpiqA?t=770


"""
from contextlib import contextmanager
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('sample.txt', 'w') as f:
    f.write('Random Text written by Joseph YU on Christamas Day.')

print(f.closed)
"""


# 🎯🧐 To-Review: catching errors, tear-down and finally
# Set up & Tear down




import os
from contextlib import contextmanager
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())

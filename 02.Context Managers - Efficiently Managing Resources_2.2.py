"""
🎯 how to NOT overwite existing file? how to start from the end and do NOT impact any existing content

"""

# use this contextmanager "decorator" to to decorate a generator function
from contextlib import contextmanager


with open('sample.txt', 'w') as f:
    f.write('whatever that might be')


class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)

        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with OpenFile('sample.txt', 'w') as f:
    f.write('This something NEW')

print(f.closed)

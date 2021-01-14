# context manager -> properly manage resources,
# we can specify exactly what we want to set up and tear down
# when working with certain objects

# keyword: setUp and tearDown

# Context mangaer is the recommended way of working with files/DB (resources)


# Context manager starts with a "with" statement at the beginning
# 👍 we no longer has to close down the file any more

# Random Text written by Joseph YU on Christamas Day.
# Are we gonna over-write the original file?

with open('sample.txt', 'w') as f:
    f.write('whatever that might be')


class OpenFile:

    # init method -> accept the arguments we pass into our class
    # filename -> what we want to work with
    # mode -> opening this file for reading/writing/updating...

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # setUp: open our file here
    # Creating a new instance variable "self.file": instance variable
    # inherit variables from the __init__
    # 👀 always indentation for the def - return statement
    def __enter__(self):
        self.file = open(self.filename, self.mode)

        return self.file

    # tearDown
    # There is () in the end - to take on action to close the file
    # It's an action towards soemthing! NOT an attribute of something!
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

"""
This week, we're going to create a class that I call DirFIleHash. The idea is that you create an instance of DirFileHash by passing a directory name:

    d = DirFileHash('/etc/')

You can then get the MD5 hash of any file in this directory by putting it in square brackets:

    print(d['passwd'])

This will return the 32-character hexadecimal MD5 hash value for the contents of /etc/passwd.

"""

import hashlib, os
from hashlib import md5


class DirFileHash:
    def __init__(self, dirname):
        self.dirname = dirname

    def __getitem__(self, file):
        fullname = os.path.join(self.dirname, file)
        if os.path.exists(fullname) and os.path.isfile(fullname):
            result = hashlib.md5()
            result.update(open(fullname, "rb").read())
            return result.hexdigest()


d = DirFileHash("/etc/")
print(d["passwd"])

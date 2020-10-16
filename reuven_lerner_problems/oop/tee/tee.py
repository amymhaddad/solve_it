"""
Create a class that accepts multiple file-like objects. 

"""

import sys, os

import tee


class Tee:
    def __init__(self, *file_like_obj):
        self.file_like_obj = file_like_obj

    def write(self, text):
        for file in self.file_like_obj:
            sys.stdout.write(text)

        for file in self.file_like_obj:
            file.write(text)

    def writelines(self, text):

        for file in self.file_like_obj:
            sys.stdout.writelines(text)

        for file in self.file_like_obj:
            file.writelines(text)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for file in self.file_like_obj:
            file.close()


f1 = open("out.txt", "w")
f2 = open("out2.txt", "w")
t = Tee(f1, f2)

f3 = open("out.txt", "w")
f4 = open("out2.txt", "w")

with Tee(f3, f4) as t2:
    t2.write("!!!xyz\n")
    t2.write("???xyz\n")

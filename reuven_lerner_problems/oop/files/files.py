import os, glob

dir = "/etc/*"


def filefunc(dirname, func):
    success_dict = {}
    failure_dict = {}

    for filename in glob.glob(dir):
        file_name = os.path.basename(filename)
        try:
            success_dict[filename] = func(filename)
        except Exception as e:
            failure_dict[filename] = e
    return success_dict, failure_dict


def file_len(filename):
    return open(filename).readline()


print(filefunc(dir, file_len))

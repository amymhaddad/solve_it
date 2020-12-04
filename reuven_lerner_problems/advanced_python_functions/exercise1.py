"""
(1) Write a function, transform_files, that takes any number
    of filenames as arguments, and two optional keyword-only
    arguments:

    - suffix, which defaults to the string "new"
    - function, which defaults to len

    The function will iterate over the filenames it receives, applying
    the function to each filename.  The output from the function will
    be stored in a new file of the same name as the original filename,
    but with the suffix appended.

    So if we call

        transform_files('a.txt', 'b.txt', 'c.txt')

    The files a.txt.new and b.txt.new and c.txt.new will all
    have the content "5", because the filename is 5 characters
    long.  You can pass whatever function you want instead.
    """


def transform_files(*args, suffix="new", function=len):
    for file in args:
        with open(f"{file}.{suffix}", "w") as f_obj:
            f_obj.write(str(function(file)))


print(transform_files("a.txt", "b.txt", "c.txt"))

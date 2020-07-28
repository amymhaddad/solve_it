
For the purposes of this exercise, we'll be looking at one of my favorite files, which I call "mini-access-log.txt".  It is an excerpt from the Apache HTTP server on my computer (lerner.co.il) from several years ago.  You can view and download it from here:

    https://gist.github.com/reuven/5875971

Each line of this logfile looks like the following:
67.218.116.165 - - [30/Jan/2010:00:03:18 +0200] "GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)"

The exercise is to write a function that, when given a filename, returns a list of dictionaries.  Each dict should have the following keys:
ip_address, containing the IP address
timestamp, containing the timestamp (not including the square brackets, but everything inside of them)
request, containing the HTTP request (not including the double quotes, but everything inside of them)

Thus, the above line from mini-access-log.txt would look like this:
   {'ip_address': '67.218.116.165',
     'timestamp': '30/Jan/2010:00:03:18 +0200',
     'request': 'GET /robots.txt HTTP/1.0'}

At the heart of this class will be the same list of dicts.  That is, when we create an instance of our LogDicts class, we'll load the entire file into memory.  (You can assume that the logfile isn't too big; perhaps in the future, we'll talk about "chunking" files that are too load to read all at once.)  Then, with that in place, we'll be able to invoke a number of different methods:
   ld = LogDicts('mini-access-log.txt')

Again, creating an instance of LogDicts will load the list of dicts into the object, making them available for our use.

    ld.dicts(key=None)      # return the list of dicts, same as last week's exercise
    ld.iterdicts(key=None)  # returns an iterator of dicts, rather than the list all at once
   ld.earliest()   # returns the dict with the earliest timestamp
    ld.latest()     # returns the dict with the latest timestamp

In order for these two methods to work, you'll need to turn the timestamp into an actual time object. I'd suggest using time.strptime, although there are alternatives on PyPI that you might prefer, such as "arrow".
   ld.for_ip(ip_address, key=None)   # returns all records for a particular IP address
    ld.for_request(text, key=None)    # returns all records whose request contains text

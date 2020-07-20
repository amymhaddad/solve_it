"""
Each line of this logfile looks like the following:
67.218.116.165 - - [30/Jan/2010:00:03:18 +0200] "GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)"

The exercise is to write a function that, when given a filename, returns a list of dictionaries.  
Each dict should have the following keys:
* ip_address, containing the IP address
* timestamp, containing the timestamp (not including the square brackets, but everything inside of them)
* request, containing the HTTP request (not including the double quotes, but everything inside of them)
"""
# Approach 1
def get_file_data(file):

    all_lines = []
    with open(file) as f_obj:
        lines = f_obj.readlines()

        for line in lines:
            each_line = "".join(line.split("\n"))
            all_lines.append(each_line)
    return all_lines


file_data = get_file_data("text.txt")


def get_logfile_data(file_data):
    all_files = []

    for line in file_data:
        ip_address = line.split()[0]

        timestamp_start = line.index("[") + 1
        timestamp_end = line.index("]")
        timestamp = line[timestamp_start:timestamp_end]

        request_start = line.index('"') + 1
        request_end = line[request_start:].find('"')
        request = line[request_start : request_start + request_end]

        logfile = {
            "ip_address": ip_address,
            "timestamp": timestamp,
            "request": request,
        }
        all_files.append(logfile)
    return all_files


# Approach 2
import re

file_name = "files.txt"
store_logfiles = []


def read_lines_from_file(file_name):
    all_lines = []
    with open(file_name) as f_obj:
        lines = f_obj.readlines()

        for line in lines:
            each_line = "".join(line.split("\n"))
            all_lines.append(each_line)
    return all_lines


total_logfiles = read_lines_from_file(file_name)


def parse_data(total_logfiles):

    all_files = []
    for file in total_logfiles:
        logfiles = {}
        index_to_end_string = 6
        remove_dashes = re.sub(r'(- -\s\W)|(\W\s")| \d{3}\s\d+"', " ", file)
        parsed_line = remove_dashes.split()[:index_to_end_string]

        logfiles["ip_address"] = parsed_line[0]
        logfiles["timestamp"] = parsed_line[1]
        logfiles["request"] = "".join(parsed_line[2:])

        all_files.append(logfiles)

    return all_files

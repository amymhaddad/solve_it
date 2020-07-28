import operator, arrow


class LogDicts:
    def __init__(self, filename):
        self.format = "DD/MMM/YYYY:HH:mm:ss Z"
        self._dicts = [self.get_logfile_data(line) for line in open(filename)]

    def get_logfile_data(self, line):
        ip_address = line.split()[0]

        timestamp_start = line.index("[") + 1
        timestamp_end = line.index("]")
        timestamp = line[timestamp_start:timestamp_end]

        request_start = line.index('"') + 1
        request_end = line[request_start:].find('"')
        request = line[request_start : request_start + request_end]

        return {
            "ip_address": ip_address,
            "timestamp": timestamp,
            "request": request,
        }

    def dicts(self, key=None):
        return list(self.iterdicts(key=key))

    def iterdicts(self, key=None):
        if key:
            return (item for item in sorted(self._dicts, key=key))

        else:
            return (item for item in self._dicts)

    def _get_timestamps(self):
        all_timestamps = []
        for items in self._dicts:
            timestamp = items["timestamp"]
            all_timestamps.append(arrow.get(timestamp, self.format))
        return all_timestamps

    def earliest(self):
        return min(self._get_timestamps())

    def latest(self):
        return max(self._get_timestamps())

    def get_ip_address(self, key=None):
        if key:
            return [dict for dict in self._dicts if dict["ip_address"] == key]
        return self._dicts

    def get_request(self, key=None):
        if key:
            return [dict for dict in self._dicts if dict["request"] == key]
        return self._dicts
